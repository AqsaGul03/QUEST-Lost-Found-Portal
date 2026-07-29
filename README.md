# University Lost & Found Portal

A centralized web platform for QUEST Nawabshah students to report and recover lost belongings on campus.

**Group:** ByteBuilders
**Course:** Software Engineering, 2025–2026
**Institution:** Quaid-e-Awam University of Engineering, Science and Technology (QUEST), Nawabshah

## Project Overview

Students frequently lose items on campus (ID cards, phones, wallets, backpacks) with no central way to report or recover them. This portal lets any student:

- Report a lost item with full details
- Report a found item so the owner can be contacted
- Search and browse all reports, filtered by item name, location, or type

## Team Members

| Name | Role | Responsible For |
|---|---|---|
| Muskan | Backend & Database Developer | `app.py` (Flask routes, database logic) |
| Aqsa Gul | Frontend Developer — Home & Confirmation Pages | `index.html`, `success.html` |
| Bisma | Frontend Developer — Forms | `report-lost.html`, `report-found.html` |
| Mahgul | Frontend Developer — Search Module | `search.html` |
| Fatima | UI/UX Designer | `style.css` |

## Features

- Report a lost item with full details
- Report a found item so the owner can be contacted
- Search items by name or filter by campus location
- View reporter's contact details for each report
- Simple, student-friendly interface

## Technologies Used

- **Backend:** Python (Flask)
- **Database:** SQLite
- **Frontend:** HTML5, CSS3, JavaScript (vanilla)
- **Version Control:** Git & GitHub

## Repository Structure

```
QUEST-Lost-Found-Portal/
├── app.py                  → Backend logic & database routes
├── templates/
│   ├── index.html          → Home page
│   ├── report-lost.html    → Report Lost form
│   ├── report-found.html   → Report Found form
│   ├── search.html         → Search & browse reports
│   └── success.html        → Submission confirmation
├── static/
│   └── style.css           → All styling
└── database.db             → SQLite database (auto-created on first run)
```

## How to Run Locally

1. Install Flask:
   ```
   pip install flask
   ```
2. Run the app:
   ```
   python app.py
   ```
3. Open in browser:
   ```
   http://127.0.0.1:5000/
   ```

## Academic Info

Submitted to: Sir Zahid Hussain Abro
Course: Software Engineering
Academic Year: 2025–2026
