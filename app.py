# <!--
#   University Lost & Found Portal — app.py (Backend / Main Application)
#   Created by: Muskan (24IT-46) — Backend Developer
#   Group: ByteBuilders | QUEST Nawabshah | SE 2025-2026
# -->

from flask import Flask, render_template, request, redirect, url_for

import sqlite3

app = Flask(__name__)
DB_NAME = 'database.db'


def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # lets us access columns by name
    return conn


def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            item_name TEXT NOT NULL,
            description TEXT NOT NULL,
            date TEXT NOT NULL,
            location TEXT NOT NULL,
            custody TEXT,
            contact TEXT NOT NULL,
            reporter_name TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


# init_db() ab yahin call ho raha hai (module load pe), sirf __main__ block
# mein nahi. Isse table hamesha ban jayega, chahe app kisi bhi tareeqe se
# run ho (flask run, gunicorn, ya python app.py).
init_db()


def get_required_fields(fields):
    """
    Form fields ko safely read karta hai.
    Agar koi required field missing/empty ho, to (None, error_message) return
    karta hai, warna (data_dict, None) return karta hai.
    Isse KeyError se app crash hone se bach jata hai.
    """
    data = {}
    for field in fields:
        value = request.form.get(field, '').strip()
        if not value:
            return None, f"'{field}' field is required."
        data[field] = value
    return data, None


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/report-lost')
def report_lost():
    return render_template('report-lost.html')


@app.route('/report-found')
def report_found():
    return render_template('report-found.html')


@app.route('/submit-lost', methods=['POST'])
def submit_lost():
    data, error = get_required_fields(
        ['item', 'description', 'date', 'location', 'contact', 'name']
    )
    if error:
        return render_template('report-lost.html', error=error)

    conn = get_db_connection()
    conn.execute(
        '''INSERT INTO items (type, item_name, description, date, location, custody, contact, reporter_name)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
        ('lost',
         data['item'],
         data['description'],
         data['date'],
         data['location'],
         '',
         data['contact'],
         data['name'])
    )
    conn.commit()
    conn.close()
    return redirect(url_for('success'))


@app.route('/submit-found', methods=['POST'])
def submit_found():
    data, error = get_required_fields(
        ['item', 'description', 'date', 'location', 'custody', 'contact', 'name']
    )
    if error:
        return render_template('report-found.html', error=error)

    conn = get_db_connection()
    conn.execute(
        '''INSERT INTO items (type, item_name, description, date, location, custody, contact, reporter_name)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
        ('found',
         data['item'],
         data['description'],
         data['date'],
         data['location'],
         data['custody'],
         data['contact'],
         data['name'])
    )
    conn.commit()
    conn.close()
    return redirect(url_for('success'))


@app.route('/search')
def search():
    # Ab ye route asal mein search bhi kar sakta hai (agar koi query ho),
    # warna sab items dikhata hai — jaisa pehle tha.
    query = request.args.get('q', '').strip()
    conn = get_db_connection()
    if query:
        items = conn.execute(
            '''SELECT * FROM items
               WHERE item_name LIKE ? OR location LIKE ? OR description LIKE ?
               ORDER BY id DESC''',
            (f'%{query}%', f'%{query}%', f'%{query}%')
        ).fetchall()
    else:
        items = conn.execute('SELECT * FROM items ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('search.html', items=items, query=query)


@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)
