# GRIET Library Management System

A modern and user-friendly Library Management System built with Streamlit.

## Features

- User authentication (Login/Register)
- Book browsing and searching
- Book borrowing and returning
- Transaction history
- Fine management
- Admin panel for library management
- Book recommendations
- Statistics and analytics

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
streamlit run lms.py
```

## Default Admin Credentials

- Username: admin
- Password: admin123

## Data Storage

The application stores data in JSON files in the `srp` directory:
- users.json
- books.json
- borrowings.json
- transactions.json
- fines.json
- return_requests.json 