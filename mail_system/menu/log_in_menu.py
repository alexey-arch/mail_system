from menu.basemenu import*
from menu.constatn import*

class Log_In(BasseMenu):
    log_in_option = (
        Option("2", "Continue"),
        Option("3", "back"),
    )
    
    def __init__(self):
        super().__init__('Log in', self.log_in_option)

    def show(self):
        print("_-"*5, self.title, "-_"*5)
        for option in self.options:
            print(f"[{option.index}] - {option.title}.")