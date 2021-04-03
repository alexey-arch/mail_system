import json
from models.users import User
class Storage:
    inst = None
    users = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls.inst is None:
            cls.inst = object.__new__(cls)
            cls.users = []
        return cls.inst

    def fill_storage(self):
        with open('data.json', 'r') as file:
            data = json.load(file)
        self.users = [
            User.from_dict(user_data)
            for user_data in data
        ]
    
    def fill_json(self):
        storage = Storage()
        data = []

        for item in storage.users:
            obj = {
                'username' : item.username,
                'password' : item.password
            }

            data.append(obj)
        
        with open('data.json', 'w') as file:
            json.dump(data, file , indent=4, sort_keys=False)