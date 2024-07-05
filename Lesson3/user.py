class User:
    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln

    def sayFirstName(self):
        print(self.first_name)

    def sayLastName(self):
        print(self.last_name)

    def sayFN_LN(self):
        print(self.first_name, self.last_name)
