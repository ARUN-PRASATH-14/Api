from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel  #from library import class : format

app = FastAPI()


API_KEY = "12345ABCDEF"

@app.middleware("http")
async def check_apikey(request, call_next):
    key = request.headers.get("X-API-KEY")
    if key != API_KEY:
        return JSONResponse(status_code=401, content={"error": "unauthorized"})
    return await call_next(request)



@app.get("/welcome")
def welcome():
    return {"message": "welcome to my Api!!"}

@app.get("/user")
def user_profile():
    return{
        "name":"Arun",
        "Age":20,
        "Gender":"Male",
        "phone number":9342792472
    }

@app.get("/user/{user_id}")
def user_profile(user_id: int):
    if(user_id == 1):
        return{
            "name":"David",
            "gender":"Male"
        }
    else:
        return{
            "name":"mary"+str(user_id),
            "gender":"female"
        }
    
# {
#     "name":"Adam",
#     "age":25,
#     "email":"adam123@gmail.com"
# },

class User(BaseModel):
    name : str
    age : int
    email : str

users = []

@app.post("/users")
def create_user(user: User):
    users.append(user.dict())
    return {"message" : "User added Successfully", "Total-Users":len(users)}