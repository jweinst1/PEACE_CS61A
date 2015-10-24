#class that demonstrates self value.

class intbot(int):
    def __init__(self):
        int.__init__(self)
    def show_value(self):
        return self
