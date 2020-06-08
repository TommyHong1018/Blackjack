class Cards():
    number = 0
    type = ""

    def __init__(self, number, type):
        self.number = number
        self.type = type

    def getnumber(self):
        return self.number

    def gettype(self):
        return self.type

    def display(self):
        print(self.type + str(self.number))
