from Deck import Deck


class Player(Deck):
    Name = " "
    Score = 0

    def Drawcard2(self, deck):
        Temp = deck.Drawcard()
        self.Rawdeck.append(Temp)

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

    def Summary(self):
        self.Score = 0
        iterator = iter(self.Rawdeck)
        haselement = False
        while not haselement:
            try:
                Temp = next(iterator)
                self.Score = self.Score + Temp.getnumber()
            except StopIteration:
                haselement = True

