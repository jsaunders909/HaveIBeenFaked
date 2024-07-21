"""This file will be responsible for adding helper methods for the parser"""
from hibf_lib import add_front_image, add_right_image, add_left_image, check_image
import numpy as np
from cv2 import imread, imdecode

image_funcs = {
    "left": add_left_image,
    "right": add_right_image,
    "front": add_front_image
}

def add_image(username:str, image_bytes:bytes, image_mode:str) -> bool:
    uid = username
    image = imdecode(np.frombuffer(image_bytes, np.uint8), -1)
    name = username

    return image_funcs[image_mode](uid, image, name, "../face_db")

def scan_for_match(image_bytes:bytes) -> list:
    image = imdecode(np.frombuffer(image_bytes, np.uint8), -1)
    return check_image(image, "../face_db")
