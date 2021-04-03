from models.storage import Storage
from models.users import *
from utils import get_input_function
import re
from models.users import get_data_from_json

class Check_In:
    def sign_up(self):
        storage = Storage()
        numbers = re.compile('[^A-Z^a-z]')
        data_from_json = get_data_from_json()
        while True:
            user_input = input('Login: ')
            if user_input[0] in ('0,1,2,3,4,5,6,7,8,9'):
                print('Name must not start with a number!')
            elif len(user_input) < 12:
                print('Name too short!')
            elif user_input[-8] not in ('@') and user_input[-3] not in ['.']:
                print('Be sure to specify "@ mail.ru" !')
            else:
                log = {
                    'username':user_input
                }
                for i in data_from_json:
                    if log['username'] == i['username']:
                        print('login unavailable!')
                        break
                else:
                    username = user_input
                    break
                
        while True:
            user_input = input('Password: ')
            if len(user_input) < 8:
                print('Weak password!')
            elif len(user_input) >= 8:
                if user_input.islower() or user_input.isupper() or user_input.isdigit():
                    print('Weak password!')
                else:
                    password = user_input
                    break
        storage.fill_storage()
        storage.users.append(
            User(username, password)
        )
        storage.fill_json()