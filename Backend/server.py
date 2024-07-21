from fastapi import FastAPI, Form, File
from fastapi.responses import JSONResponse
from typing import Annotated
from database import auth_db
from recog_helper import add_image

app = FastAPI()

@app.get("/")
def index():
    return "Hello World"

@app.get("/signup/")
def signup(username: Annotated[str, Form], password: Annotated[str, Form]):
    if auth_db.add_user(username, password):
        return JSONResponse({"status": True})
    else:
        return JSONResponse({"status": False})

@app.get("/login/")
def login(username: Annotated[str, Form], password: Annotated[str, Form]):
    user_password = auth_db.get_user_by_username(username)
    if user_password and user_password == password:
        return JSONResponse({"status": True})
    return JSONResponse({"status": False})

@app.post("/faces/front")
def add_front_face(username: Annotated[str, Form()], image: Annotated[bytes, File()]):
    result = add_image(username, image, "front")
    return JSONResponse({"status": result})

@app.post("/faces/left")
def add_left_face(username: Annotated[str, Form()], image: Annotated[bytes, File()]):
    result = add_image(username, image, "left")
    return JSONResponse({"status": result})
    

@app.post("/faces/right")
def add_right_face(username: Annotated[str, Form()], image: Annotated[bytes, File()]):
    result = add_image(username, image, "right")
    return JSONResponse({"status": result})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app='server:app', host="0.0.0.0", reload=True)
