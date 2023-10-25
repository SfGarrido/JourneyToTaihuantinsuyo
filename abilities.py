class Abilities:
    def __init__(self, aname, cd, func):
        self.name = aname
        self.cooldown = cd
        self.func = func

class Dash(Abilities):

    def __init__(self):
        Abilities.__init__(self, "dash", 2, self.func)
        self.active = False
        self.current = 0
    def func(self):
        print("Do smth")
