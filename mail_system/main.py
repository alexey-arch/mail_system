from menu.mainmenu import*
from menu.basemenu import*
from menu.constatn import*
from menu.sign_up_menu import*
from menu.log_in_menu import*
from check_in import Check_In
from log_in import Log_Ing
from models.users import*

def get_user_input(options):
    available_inputs = [
        option[0]
        for option in options
    ]

    while True:
        user_option = input('Enter option id: ')
        if user_option in available_inputs:
            break
        else:
            print(
                'Invalid option! Chose from', 
                available_inputs[0], 'to', 
                available_inputs[-1]
            )
    return user_option

def main():
    main_menu = Main_Menu()
    sign_up = Sign_Up()
    log_in = Log_In()
    check_in = Check_In()
    log = Log_Ing()

    main_menu.show()
    user_input = get_user_input(main_menu_options)

    if user_input == SIGN_UP:
        check_in.sign_up()
        print("\n-registration completed ✓\n")
        sign_up.show()
        user_input = get_user_input(sign_up_menu_options)
        if user_input == CONTINUE:
            print("✵_Welcome to the site_✵")

        if user_input == BACK:
            main()

    elif user_input == LOG_IN:
        while user_input != BACK:
            log.log_ing()
            log_in.show()
            user_input = get_user_input(log_in_menu_option)
            if user_input == CONTINUE:
                print("✵_Welcome to the site_✵")
                break

            if user_input == BACK:
                main()

    elif user_input == EXIT:
        print("Good bay!")
        exit(0)
    

if __name__ == '__main__':
    main()
        


