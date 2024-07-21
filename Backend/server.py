from fastapi import FastAPI, Form, File
from fastapi.responses import JSONResponse
from typing import Annotated
from database import auth_db, count_db
from recog_helper import add_image, scan_for_match

app = FastAPI()

@app.get("/")
def index():
    return "Hello World"

@app.get("/signup/")
def signup(username: Annotated[str, Form], password: Annotated[str, Form]):
    if auth_db.add_user(username, password):
        return JSONResponse({"success": True})
    else:
        return JSONResponse({"success": False})

@app.get("/login/")
def login(username: Annotated[str, Form], password: Annotated[str, Form]):
    user_password = auth_db.get_user_by_username(username)
    if user_password and user_password == password:
        return JSONResponse({"success": True})
    return JSONResponse({"success": False})

@app.post("/faces/front")
def add_front_face(username: Annotated[str, Form()], image: Annotated[bytes, File()]):
    result = add_image(username, image, "front")
    return JSONResponse({"success": result})

@app.post("/faces/left")
def add_left_face(username: Annotated[str, Form()], image: Annotated[bytes, File()]):
    result = add_image(username, image, "left")
    return JSONResponse({"success": result})
    

@app.post("/faces/right")
def add_right_face(username: Annotated[str, Form()], image: Annotated[bytes, File()]):
    result = add_image(username, image, "right")
    return JSONResponse({"success": result})

@app.get("/facecheck/")
def face_check(username: Annotated[str, Form()]):
    number_of_matches = count_db.get_count_from_username(username)
    if number_of_matches:
        return JSONResponse({"success": True, "message": f"Found {number_of_matches} matches for {username}."})
    return JSONResponse({"success": False, "message": f"No matches found for {username}."})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app='server:app', host="0.0.0.0", reload=True)
