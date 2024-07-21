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
                count_db.increment_user_count(username, 0)
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

    def increment_user_count(self, username: str, value: int=1) -> None:
        with open(self.database, "r") as f:
            data = load(f)
            if username in data:
                data[username] += 1
            else:
                data[username] = value
            with open(self.database, "w") as f:
                dump(data, f, indent=4)

    def get_count_from_username(self, username: str) -> int | None:
        with open(self.database, "r") as f:
            data = load(f)
            try:
                return data[username]
            except KeyError:
                return None
        
count_db = AnotherDatabase()
auth_db = Database()