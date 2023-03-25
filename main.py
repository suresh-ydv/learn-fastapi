from fastapi import FastAPI, Response, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

'''*** Basic fastapi code ***'''


class SignupFields(BaseModel):
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
              "name": "Suresh",
              "phone_no": "98044*****",
              "description": "Never give up",
              "email": "ydvsuresh40242@gmail.com",
              "password": "password"
              }]


@app.post("/signup")
async def user_signup(items: SignupFields):
    # print(items)
    # print(items.dict())
    new_signup = items.dict()
    user_data.append(new_signup)
    # print(user_data)
    return {"new_post": new_signup}


@app.get("/user-details")
async def user_details():
    return {"data": user_data}


def user_find(id):
    for p in user_data:
        if p["id"] == id:
            return p


@app.get("/find_user/{id}")
async def find_user(id, response: Response):
    Details = user_find(int(id))
    if not Details:
        # response.status_code = 404
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": f"id: {id} not found!"}
    return {"UserDetails": Details}


'''**** END of Basic fastapi Code ***'''
