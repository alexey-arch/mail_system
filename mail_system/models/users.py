import json

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    @classmethod
    def to_dict(inst):
        return {
            'username' : inst.username,
            'password' : inst.password
        }

def get_data_from_json():
    with open('data.json', 'r') as f:
        data = json.load(f)
        return data
