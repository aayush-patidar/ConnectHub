# ConnectHub – Social Media Backend API

A RESTful social media backend built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy**. The project focuses on secure authentication using JWT and user-specific authorization for managing posts.

## 🚀 Tech Stack

* Python
* FastAPI
* PostgreSQL
* SQLAlchemy ORM
* Pydantic
* JWT Authentication (`python-jose`)
* Passlib (bcrypt)
* Uvicorn

---

## ✨ Features Implemented

### Authentication

* User registration
* Secure password hashing with bcrypt
* User login
* JWT access token generation
* Protected routes using Bearer Token authentication

### Posts

* Create a new post
* Get all posts created by the authenticated user
* Update only your own posts
* Delete only your own posts

### Authorization

* Users can only modify or delete their own posts.
* Unauthorized update/delete attempts return appropriate HTTP status codes.

---

## 📂 Project Structure

```text
connecthub/
│
├── app/
│   ├── routers/
│   │   ├── auth.py
│   │   ├── users.py
│   │   └── posts.py
│   │
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   ├── oauth2.py
│   ├── schemas.py
│   ├── utils.py
│   └── main.py
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🔐 Authentication Flow

```text
User Login
      │
      ▼
Verify Credentials
      │
      ▼
Generate JWT Token
      │
      ▼
Client stores token
      │
      ▼
Authorization: Bearer <token>
      │
      ▼
Protected Route
      │
      ▼
Current User Retrieved
```

---

## 📌 API Endpoints

### Authentication

| Method | Endpoint | Description                 |
| ------ | -------- | --------------------------- |
| POST   | `/login` | Login and receive JWT token |
| POST   | `/users` | Register a new user         |

### Posts

| Method | Endpoint     | Description                    |
| ------ | ------------ | ------------------------------ |
| POST   | `/post`      | Create a post                  |
| GET    | `/post`      | Get authenticated user's posts |
| PUT    | `/post/{id}` | Update your own post           |
| DELETE | `/post/{id}` | Delete your own post           |

---

## 🛡️ Authorization Rules

* Authentication is required for all post endpoints.
* A user can only access and modify their own posts.
* `user_id` is obtained from the JWT token, not from the request body.

---

## 📈 Upcoming Features

* Like / Unlike Posts
* Comments
* Follow / Unfollow Users
* Personalized Feed
* Pagination
* Search
* Redis Caching
* Docker
* Automated Testing
* Deployment

---

## ▶️ Run Locally

1. Clone the repository.

2. Create a virtual environment.

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure the `.env` file with your PostgreSQL database credentials and JWT settings.

5. Start the server:

```bash
uvicorn app.main:app --reload
```

6. Open the API documentation:

```
http://127.0.0.1:8000/docs
```

---

## 📄 License

This project is developed for learning backend development with FastAPI and PostgreSQL.
