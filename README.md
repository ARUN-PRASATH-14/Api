
FastAPI User Service
A simple API to manage users with authentication and validation.

🛠️ Setup & Run
Install requirements:

Bash
pip install fastapi uvicorn
Run the server:

Bash
uvicorn main:app --reload
(Make sure your python file is named main.py)

🔑 Authentication
Important: Every request requires this header, or it will be rejected.

Key: X-API-KEY
Value: 12345ABCDEF

📡 Endpoints
GET /welcome - Check if API is running.
GET /user - Get a static user profile.

GET /user/{id} - Get user details by ID.

POST /users - Add a new user (Requires JSON body: name, age, email).
