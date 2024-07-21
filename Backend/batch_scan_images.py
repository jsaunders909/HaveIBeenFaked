from database import auth_db, count_db
from recog_helper import scan_for_match
from os import listdir

def scan_images_for_matches():
    image_folder = "./images/"

    users = {}

    for image_file in listdir(image_folder):
        with open(image_folder + image_file, "rb") as f:
            image_bytes = f.read()

        names_in_image = scan_for_match(image_bytes)

        if names_in_image:
            for name in names_in_image:
                users.setdefault(name, [])
                users[name].append(image_file)
    
    for name, images in users.items():
        count_db.add_user_and_refs(name, images)
    
if __name__ == "__main__":
    scan_images_for_matches()
