class Abilities:
    def __init__(self, aname, cd, func):
        self.name = aname
        self.cooldown = cd
        self.func = func

class Dash(Abilities):

    def __init__(self):
        Abilities.__init__(self, "dash", 2, self.func)

    def func(self):
        print("Do smth")
