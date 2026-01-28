import random
import time
class CLIView:
    def __init__(self):
        self.name = ""
    def get_input(self):
        time.sleep(.1)
        return random.randint(0,6)