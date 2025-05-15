# FastAPI POC

This project is a FastAPI-based Proof of Concept (POC) for user authentication, todo management, and user administration. It demonstrates the use of FastAPI, SQLAlchemy, Alembic, JWT authentication, and PostgreSQL.

## Features
- User registration and authentication (JWT-based)
- Admin and regular user roles
- CRUD operations for todo items (per user)
- User profile management
- Alembic migrations for database schema

## Project Structure
- `main.py`: FastAPI app entry point
- `router/`: API route definitions (auth, user, todo)
- `models/`: SQLAlchemy ORM models
- `schemas/`: Pydantic schemas for request/response
- `repository/`: Database access logic
- `service/`: Business logic
- `utils/`: Utility functions (auth, security, db init)
- `config/`: Database configuration
- `dependancy/`: Dependency injection for authentication
- `alembic/`: Database migrations

## Setup
1. **Clone the repository**
2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure your database**
   - Update the database URL in `config/database.py` as needed.
5. **Run Alembic migrations**
   ```bash
   alembic upgrade head
   ```
6. **Start the FastAPI server**
   ```bash
   uvicorn main:app --reload
   ```

## API Endpoints

### Auth Endpoints (`/auth`)
| Method | Path         | Description                       |
|--------|--------------|-----------------------------------|
| POST   | /auth/login  | User login, returns JWT tokens    |
| POST   | /auth/refresh| Refresh access token              |

### User Endpoints (`/users`)
| Method | Path                    | Description                                 |
|--------|-------------------------|---------------------------------------------|
| POST   | /users                  | Register a new user                         |
| GET    | /users/profile          | Get current user's profile                  |
| PATCH  | /users/profile          | Update current user's profile               |
| GET    | /users                  | List all users (admin only)                 |
| GET    | /users/email/{email}    | Get user by email (admin only)              |
| GET    | /users/username/{username}| Get user by username (admin only)         |
| GET    | /users/{user_id}        | Get user by ID (admin or self)              |
| PATCH  | /users/{user_id}        | Update user by ID (admin or self)           |
| DELETE | /users/{user_id}        | Delete user by ID (admin only)              |

### Todo Endpoints (`/todos`)
| Method | Path            | Description                        |
|--------|-----------------|------------------------------------|
| POST   | /todos/         | Create a new todo                  |
| GET    | /todos/         | Get all todos for current user     |
| GET    | /todos/{todo_id}| Get a todo by ID                   |
| PUT    | /todos/{todo_id}| Update a todo by ID                |
| DELETE | /todos/{todo_id}| Delete a todo by ID                |

## Live Server
```
https://fastapi-poc-j61h.onrender.com/docs#/
```

## License
This project is for demonstration purposes only.
