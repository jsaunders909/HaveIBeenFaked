from json import load, dump, loads, dumps

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
                with open(self.database, "w") as f:
                    dump(data, f, indent=4)
        return True

    def get_user_by_username(self, username: str) -> str:
        with open(self.database, "r") as f:
            data = load(f)
            return data[username]
        
auth_db = Database()