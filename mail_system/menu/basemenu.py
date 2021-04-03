from menu.constatn import *

main_menu_options = (
    (SIGN_UP, 'Sign up'),
    (LOG_IN, 'Log in'),
    (EXIT, 'Exit')
)
sign_up_menu_options = (
    (CONTINUE, 'Continue'),
    (BACK, 'Back')
)
log_in_menu_option = (
    (CONTINUE, 'Continue'),
    (BACK, 'Back')
)

class Option:
    def __init__(self, index, title):
        self.index = index
        self.title = title


class ActiveOption(Option):
    def __init__(self, index, title, action):
        super().__init__(index, option)
        self.action = action

    def perform_action(self):
        self.action


class BasseMenu:
    def __init__(self, title, options=None):
        self.title = title
        self.options = options
    
    def show(self):
        return NotImplementedError