import random

from Cards import Cards

class Deck():
    Rawdeck = []
    types = ["Spade", "Heart", "Club", "Diamond"]

    def __init__(self):
        self.Rawdeck = []

    def initdeck(self):
        n = 1
        while n<53:
            Tempnum = random.randint(1, 13)
            Temptype = random.randint(0, 3)
            Temp = Cards(Tempnum, self.types[Temptype])
            Existence = False
            i = 0
            while i<len(self.Rawdeck):
                if self.Rawdeck[i].getnumber() is Tempnum and self.Rawdeck[i].gettype() is self.types[Temptype]:
                    Existence = True
                i = i + 1

            if Existence == False:
                self.Rawdeck.append(Temp)
            n = n + 1


    def Display(self):
        iterator = iter(self.Rawdeck)
        haselement = False
        while not haselement:
            try:
                Temp = next(iterator)
                print(str(Temp.number) + Temp.type)
            except StopIteration:
                haselement = True
                print("no more element")

    def Drawcard(self):
        return self.Rawdeck.pop()
