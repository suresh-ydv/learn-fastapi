from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

'''*** Basic code for well understanding ***'''


class Sign_Up(BaseModel):
    id: int
    name: str
    phone_no: str
    description: Optional[str] = None
    email: str
    password: str


@app.get("/")
async def root():
    return {"message": "Keep learning"}


user_data = [{"id": 101,
              "name": "Raina bhai",
              "phone_no": "9804402354",
              "description": "Here is the description",
              "email": "ydvsuresh40242@gmail.com",
              "password": "password"
              }]


@app.post("/signup")
async def user_signup(items: Sign_Up):
    # print(items)
    # print(items.dict())
    new_signup = items.dict()
    user_data.append(new_signup)
    # print(user_data)
    return {"new_post": new_signup}


@app.get("/user_data")
async def user_details():
    return {"data": user_data}


def user_find(id):
    for p in user_data:
        if p["id"] == id:
            return p


@app.get("/find_user/{id}")
async def find_user(id):
    Details = user_find(int(id))
    return {"UserDetails": Details}


'''**** Try to focus on above code for basic understanding ***'''
