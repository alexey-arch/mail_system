from menu.basemenu import*
from menu.constatn import*

class Main_Menu(BasseMenu):
    log_in_menu_option = (
        Option('1', 'Sign up'),
        Option('2', 'Log in'),
        Option('0', 'Exit')
    )

    def __init__(self):
        super().__init__("Welcome", self.log_in_menu_option)

    def show(self):
        print("_-"*5, self.title, "-_"*5)
        for option in self.options:
            print(f"[{option.index}] - {option.title}.")