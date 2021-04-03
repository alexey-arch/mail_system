from menu.basemenu import*
from menu.constatn import*

class Sign_Up(BasseMenu):
    sign_up_menu_options = (
        Option("2", "Continue"),
        Option('3', 'Back'),
    )
    def __init__(self):
        super().__init__('Sign_up', self.sign_up_menu_options)

    def show(self):
        print("_-"*5, self.title, "-_"*5)
        for option in self.options:
            print(f"[{option.index}] - {option.title}.")