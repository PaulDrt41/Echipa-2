def attack():
    rasp1 =int(input("You choose to attack, what will you use? \n-------- \n Made in Heaven(1)        Tusk Act 4 (2)"))
    if (rasp == 1):
        if (bhp > 100):
            print ("it was all meant to be \n you opponent aged so much, he lost half of his health points")
            bhp = 1*bhp/2
            eng-=20
        else:
            print ("it's for all to see \n your opponent grew even older")
            bhp = 1/3*bhp
            eng-=15
    elif (rasp == 2):
        print ("the terrifying phenomenon of infinite rotation \n you lost all your energy because your horse hit you too hard")
        coef = random.random()
        bhp -= 80*coef
        eng = 0
def heal():
    if (php >= 75):
        print("you are determined to continue attacking")


