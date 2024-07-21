from json import load, dump
from typing import List

class Database:
    """This class is responsible for the JSON interface for User Auth information"""

    def __init__(self):
        self.database = "./database.json"

    def add_user(self, username: str, password: str) -> bool:
        with open(self.database, "r") as f:
            data = load(f)
            if username in data:
                return False
            else:
                data[username] = password
                count_db.add_user_and_refs(username, [])
                with open(self.database, "w") as f:
                    dump(data, f, indent=4)
        return True

    def get_password_by_username(self, username: str) -> str | None:
        with open(self.database, "r") as f:
            data = load(f)
            try:
                return data[username]
            except KeyError:
                return None
            
class AnotherDatabase:
    def __init__(self):
        self.database = "./userCount.json"

    def add_img_ref_to_user(self, username: str, img_name: str) -> None:
        with open(self.database, "r") as f:
            data = load(f)
            if username in data:
                data[username].append(img_name)
            else:
                data[username] = [img_name]
            with open(self.database, "w") as f:
                dump(data, f, indent=4)

    def get_image_refs_by_user(self, username: str) -> list | None:
        with open(self.database, "r") as f:
            data = load(f)
            try:
                return data[username]
            except KeyError:
                return None
            
    def add_user_and_refs(self, username: str, refs:List[str]):
        with open(self.database, "r") as f:
            data = load(f)
            data[username] = refs
            with open(self.database, "w") as f:
                dump(data, f, indent=4)
        
count_db = AnotherDatabase()
auth_db = Database()