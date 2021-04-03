from models.storage import Storage
from utils import get_input_function
from models.users import get_data_from_json

class Log_Ing:
    def log_ing(self):
        storage = Storage()
        a = False

        while True:
            user_input = input('Login: ')
            if user_input[0] in ('0,1,2,3,4,5,6,7,8,9'):
                print('Invalid login!')
            elif len(user_input) < 12:
                print('Invalid login!')
            elif user_input[-8] not in('@') and user_input[-3] not in ('.'):
                print('Please use "@mail.ru"!')
            else:
                login = user_input

            user_input = input('Password: ')
            password = user_input
            
            data_from_json = get_data_from_json()
            log_pass = {
                'username':login,
                'password':password
            }

            for i in data_from_json:
                if log_pass == i:
                    a = True
                    break

            if a is not True:
                print('\nnot a valid Login or Password!')
            else:    
                break    
            
            

