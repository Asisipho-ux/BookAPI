Book Management API

Overview:

This project is a RESTful API built using FastAPI that allows users to manage a collection of books. The API supports full CRUD functionality and demonstrates backend fundamentals including request validation, database integration, and API key authentication.

This project was created as part of my journey into backend development and API design, focusing on understanding how client requests interact with servers and databases.

Tech Stack:

Python
FastAPI
SQLAlchemy (ORM)
SQLite Database
Pydantic (Data Validation)
Uvicorn (ASGI Server)

Features:

Create books
Retrieve all books
Update books (Full & Partial)
Delete books
API Key authentication for protected endpoints
Persistent database storage using SQLite
Automatic request validation using Pydantic

Authentication:

Some endpoints require an API key sent via request headers.
Example header: `api-key: aS1iS2iP3hO-1a0b8c9e-9c3b-4d5e-8f2b-123456789012`

📂 Project Structure
book-api/
│
├── main.py          # API routes and application logic
├── models.py        # Database models
├── database.py      # Database configuration and connection
├── books.db         # SQLite database (auto-created)
├── requirements.txt # Project dependencies
└── README.md

Installation & Setup:

1. Clone Repository
git clone https://github.com/Asisipho-ux/BookAPI.git
cd book-api

2. Create Virtual Environment

Activate environment:

Windows (Git Bash):
source venv/Scripts/activate

Windows (CMD / PowerShell):
venv\Scripts\activate


3. Install Dependencies
pip install -r requirements.txt


4. Run Server
uvicorn main:app --reload


Access API:

Swagger Documentation:
http://127.0.0.1:8000/docs

API Endpoints:
Home
GET /
Returns welcome message.

Get All Books (Protected):
GET /books
Requires API key header.

Add Book: 
POST /books
Example request body:

{
"id": 1,
"title": "Atomic Habits",
"author": "James Clear"
}


Update Book:
PUT /books/{book_id}

Partial Update Book:
PATCH /books/{book_id}

Delete Book:
DELETE /books/{book_id}

Database:

This project uses SQLite for persistent storage.
The database file books.db is automatically created when the server runs.
Data remains stored even after restarting the application.

What I Learned:

1. Designing REST APIs
2. Implementing CRUD functionality
3. Securing endpoints with API keys
4. Connecting FastAPI to a database
5. Using SQLAlchemy ORM
6. Structuring backend projects professionally

Future Improvements:

JWT authentication
PostgreSQL integration
Docker containerization
Unit testing
Deployment to cloud (Render / Railway / AWS)

Author:

Asisipho Ndamase
Fullstack Developer | Data Analyst | Systems Optimization Specialist

LinkedIn:
http://www.linkedin.com/in/asisipho-ndamase-4a1041235
