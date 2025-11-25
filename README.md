# Library_Management_System

A Flask-based web application for managing library e-books with user authentication and role-based access control.

## Resume LaTeX Snippet

```latex
\resumeProject
      {Library Management System} 
      {Flask Web Application} 
      {Aug 2023 - Oct 2023} 
      {\href{https://github.com/mohdsamad83/Library_Management_System}{GitHub}} 
      \resumeItemListStart
         \item {\textbf{Tools \& technologies used}: Python, Flask, SQLite, SQLAlchemy, HTML/CSS, Jinja2}
         \item {Developed a full-stack library management system with \textbf{role-based authentication} supporting admin and general user access levels.}
         \item {Implemented \textbf{CRUD operations} for e-book management with features for book requests, grants, and returns, enabling efficient library resource tracking.}
    \resumeItemListEnd
```

## Features

- **User Authentication**: Login and registration system with role-based access (admin/general user)
- **Admin Dashboard**: Manage books, view requests, grant/deny book access
- **User Dashboard**: Browse available books, request books, view granted books, return books
- **E-book Management**: Create, read, update book records with SQLite database
- **Book Request System**: Users can request books, admins can grant permissions

## Tech Stack

- **Backend**: Python, Flask
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML, CSS, Jinja2 Templates

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirement.txt
   ```

2. Initialize the database (see `crud.txt` for commands):
   ```python
   from app import *
   db.create_all()
   ```

3. Create admin user (replace with your own secure credentials):
   ```python
   user1 = User(email="your_email@example.com", username="admin", password="your_secure_password", type="admin")
   db.session.add(user1)
   db.session.commit()
   ```

4. Run the application:
   ```bash
   python app.py
   ```