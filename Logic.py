from Aimbotz import Aimbotz
from Deck import Deck
from Player import Player

Player1 = Player()
Deck1 = Deck()
Aimbotz1 = Aimbotz()

Resume = True
Comdraw = True
Playdraw = True
Game = True
End = False

Player1.Score = 0
Aimbotz1.Score = 0
Deck1.Rawdeck = []
Deck1.initdeck()
Player1.Rawdeck = []
Aimbotz1.Rawdeck = []

while Resume:
    Comdraw = True
    Playdraw = True
    Game = True
    Player1.Score = 0
    Aimbotz1.Score = 0
    Deck1.Rawdeck = []
    Deck1.initdeck()
    Player1.Rawdeck = []
    Aimbotz1.Rawdeck = []

    while Game:
        print("Now your score is " + str(Player1.Score))
        print("Wanna Continue to draw?" + " Enter 1 to draw or 2 to give up drawing.")
        if Comdraw == False and Playdraw == False:
            Game = False
            break
        elif Player1.Score > 21:
            Game = False
            break
        elif Aimbotz1.Score > 21:
            Game = False
            break

        player = True
        com = True
        while player:
            Choice1 = input()
            Choice1 = int(Choice1)
            if Choice1 == 1:
                Player1.Drawcard2(Deck1)
                player = False
                break
            if Choice1 == 2:
                Playdraw = False
                player = False
                break
        while com:
            Comdraw = Aimbotz1.Drawornot(Deck1)
            com = False
            break
        Player1.Summary()
        Aimbotz1.Summary()
    if Player1.Score is Aimbotz1.Score:
        print("Tie")
    elif Player1.Score > 21:
        print("You Lose")
    elif Aimbotz1.Score > 21:
        print("You Win")
    elif Aimbotz1.Score > Player1.Score:
        print("You Lose")
        print(Aimbotz1.Score)
    elif Aimbotz1.Score < Player1.Score:
        print("You Win")
        print(Player1.Score)
    print("Wanna Resume" + " Press 1 to resume, 2 to give up")
    Choice2 = input()
    if int(Choice2) == 1:
        Resume = True
    elif int(Choice2) == 2:
        Resume = False






