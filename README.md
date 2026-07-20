#  Notes API

A simple Notes API built using **FastAPI**, **MySQL**, and **JWT Authentication**.

This project demonstrates user authentication, protected routes, and CRUD operations for notes.

---

##  Features

- User Registration
- User Login
- JWT Authentication
- Create Notes
- View Notes
- Update Notes
- Delete Notes
- Password Hashing
- Protected Routes using JWT

---

##  Tech Stack

- FastAPI
- MySQL
- Pydantic
- Python-JOSE (JWT)
- Passlib/Bcrypt
- Uvicorn

---

##  Project Structure

```
backend/
│
├── auth.py
├── db.py
│
└── routes/
    ├── register.py
    └── notes.py
```

---

#  API Endpoints

## 1. User Registration

### POST `/sign_in`

Creates a new user.

### Request Body

```json
{
    "mail_id": "user@gmail.com",
    "password": "password123"
}
```

### Response

```json
{
    "message": "User created"
}
```

---

## 2. User Login

### POST `/`

Authenticates the user and returns a JWT token.

### Request Body

```json
{
    "mail_id": "user@gmail.com",
    "password": "password123"
}
```

### Response

```json
{
    "access_token": "<JWT_TOKEN>",
    "token_type": "bearer"
}
```

---

## 3. Get Notes

### GET `/notes`

Returns all notes belonging to the logged-in user.

### Authorization

```
Bearer <JWT_TOKEN>
```

### Response

```json
[
    {
        "notes_id": 1,
        "notes": "Study FastAPI"
    },
    {
        "notes_id": 2,
        "notes": "Complete assignment"
    }
]
```

---

## 4. Add Note

### POST `/notes`

### Authorization

```
Bearer <JWT_TOKEN>
```

### Request Body

```json
{
    "current_notes": "Learn JWT Authentication"
}
```

### Response

```json
{
    "status": "Notes Added",
    "note": "Learn JWT Authentication"
}
```

---

## 5. Update Note

### PATCH `/notes`

### Authorization

```
Bearer <JWT_TOKEN>
```

### Request Body

```json
{
    "notes_id": 1,
    "current_notes": "Finish FastAPI Notes API"
}
```

### Response

```json
{
    "message": "notes updated successfully",
    "current_notes": "Finish FastAPI Notes API"
}
```

---

## 6. Delete Note

### DELETE `/notes?note_id=1`

### Authorization

```
Bearer <JWT_TOKEN>
```

### Response

```json
{
    "message": "Note deleted successfully"
}
```

---

#  Authentication

This project uses **JWT Authentication**.

1. Register a user.
2. Login to receive an access token.
3. Click **Authorize** in Swagger UI.
4. Enter:

```
Bearer <your_access_token>
```

5. Access all protected `/notes` endpoints.

---

#  Concepts Practiced

- FastAPI Routing
- APIRouter
- Pydantic Models
- CRUD Operations
- MySQL Integration
- JWT Authentication
- Password Hashing
- Dependency Injection (`Depends`)
- HTTP Exception Handling
- Protected Routes

---

#  Running the Project

Install the required packages:

```bash
pip install fastapi uvicorn mysql-connector-python python-jose passlib[bcrypt]
```

Run the server:

```bash
uvicorn main:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

