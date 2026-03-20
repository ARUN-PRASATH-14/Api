# FastAPI User Service

A simple REST API built with [FastAPI](https://fastapi.tiangolo.com/) to manage users with API key authentication and request validation.

---

## 🛠️ Setup & Run

**Install requirements:**

```bash
pip install fastapi uvicorn
```

Or using the requirements file:

```bash
pip install -r API/req.txt
```

**Run the server:**

```bash
uvicorn API.api:app --reload
```

---

## 🔑 Authentication

Every request must include the following header, or it will be rejected with a `401 Unauthorized` response.

| Header      | Value          |
|-------------|----------------|
| `X-API-KEY` | `12345ABCDEF`  |

---

## 📡 Endpoints

| Method | Endpoint       | Description                                              |
|--------|----------------|----------------------------------------------------------|
| GET    | `/welcome`     | Check if the API is running.                             |
| GET    | `/user`        | Get a static user profile.                               |
| GET    | `/user/{id}`   | Get user details by ID.                                  |
| POST   | `/users`       | Add a new user (requires JSON body: `name`, `age`, `email`). |

### Example: Add a New User

**Request body:**

```json
{
  "name": "Adam",
  "age": 25,
  "email": "adam123@gmail.com"
}
```

**Response:**

```json
{
  "message": "User added Successfully",
  "Total-Users": 1
}
```
