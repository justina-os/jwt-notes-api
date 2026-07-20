#  JWT Notes API

A secure REST API for managing personal notes built with **FastAPI**, **MySQL**, and **JWT Authentication**.

Users can create an account, log in, and perform CRUD operations on their own notes. Every endpoint is protected using JWT, ensuring users can only access their own data.

---

##  Features

- User Registration
- User Login
- JWT Authentication
- Create Notes
- View Personal Notes
- Update Existing Notes
- Delete Notes
- Request Validation using Pydantic
- User-specific authorization
- Proper HTTP error handling

---

##  Tech Stack

- Python
- FastAPI
- MySQL
- Pydantic
- JWT Authentication
- Uvicorn

---

##  Project Structure

```
backend/
│
├── routes/
│   ├── register.py
│   └── notes.py
│
├── db.py
├── jwt_handler.py
└── main.py
```

---

##  Authentication

Authentication is implemented using JWT.

### Public Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /signup | Register a new user |
| POST | /login | Login and receive a JWT access token |

### Protected Endpoints

All endpoints below require a valid JWT token.

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /notes | Retrieve all notes of the logged-in user |
| POST | /notes | Create a new note |
| PATCH | /notes/{notes_id} | Update a specific note |
| DELETE | /notes/{notes_id} | Delete a specific note |

---

##  Request Examples

### Create Note

POST `/notes`

```json
{
    "content": "Learn FastAPI"
}
```

### Update Note

PATCH `/notes/1`

```json
{
    "content": "Learn FastAPI and JWT"
}
```

---

## Sample Response

```json
{
    "message": "Note added successfully",
    "note": "Learn FastAPI"
}
```

---

##  Authorization

Each authenticated user can:

- Create their own notes
- View only their own notes
- Update only their own notes
- Delete only their own notes

Users cannot access or modify another user's notes.

---

##  Concepts Practiced

- REST API Design
- JWT Authentication
- Dependency Injection
- CRUD Operations
- MySQL Database Integration
- SQL Queries
- Request Validation with Pydantic
- HTTP Exception Handling
- FastAPI Routing

---



##  Future Improvements

- Search notes
- Pagination
- Docker support
- Unit Testing
- Note categories
- Soft delete functionality

---
