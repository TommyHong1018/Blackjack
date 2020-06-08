from Player import Player


class Aimbotz(Player):
    def Drawornot(self, deck):
        Currentscore = self.Score
        Safenumber = 0
        iterator = iter(deck.Rawdeck)
        haselement = False
        while not haselement:
            try:
                Temp = next(iterator)
                if Currentscore + Temp.getnumber() <= 21:
                    Safenumber = Safenumber + 1
            except StopIteration:
                haselement = True

        Remain = len(deck.Rawdeck)
        Prob = Safenumber / Remain
        if Prob > 0.50:
            self.Drawcard2(deck)
            print("Bots has drawn a card")
            return True
        else:
            print("Bots give up to draw")
            return False

    def Getscore(self):
        return self.Score

    def Resetscore(self):
        self.score = 0

    def Resetdeck(self):
        self.Rawdeck = []