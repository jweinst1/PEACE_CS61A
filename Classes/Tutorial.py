#class that demonstrates self value.

class intbot(int):
    def __init__(self):
        int.__init__(self)
    def show_value(self):
        return self

class student:

    def __init__(self, GPA, professor):
        self.GPA = GPA
        self.professor = professor

def x(y):
    return y