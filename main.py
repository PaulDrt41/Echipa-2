import random

#ma doare capul de la functii aaaaaah
#nici nu stiu dacai corect ce e aici sau nu

#da run fara erori dar valorile nu se schimba <- de rezolvat daca mergem pe functii cu parametrii in declaratie ex. def function(foo, bar):
#asta ar trebui sa mearga 100000% daca sar schimba valorile dupa apelul functiei

eng = 100
OHKO = 100
bhp = 100
php = 100

def attack(eng, bhp, OHKO):
    rasp =int(input("You choose to attack, what will you use? \nMade in Heaven (or grateful dead) (1)           Tusk Act 4 (2) \n: "))
    if rasp == 1:
        if bhp > 100:
            print ("it was all meant to be \n you opponent aged so much, he lost half of his health points")
            bhp = 1*bhp/2
            eng-=20
        else:
            print ("it's for all to see \n your opponent grew even older")
            bhp = 1/3*bhp
            eng-=15
    elif rasp == 2:
        print ("the terrifying phenomenon of infinite rotation \n you lost all your energy because your horse hit you too hard")
        coef = random.random()
        bhp -= OHKO*coef
        eng = 0

def heal(php, eng, OHKO):
    if php >= 75:
        print("you are determined to continue attacking")
        #aici nu isi da heal, ci trebuie sa aleaga alta actiune
    else:
        rasp2 = int(input("It seems your health bar is pretty low, what will you do? \n Crazy Diamond (1)           Zombie Horse String (2)\n: "))
        if rasp2 == 1:
            print(" Dora the Explora\n you recovered all your health points but your hand looks kind of funny now")
            php = 100
            eng-=40
            OHKO -=25
        elif rasp2 == 2:
            print("forgot what the panel said\n magicaly, the wounds you sew dissapeared")
            php += 30
            eng-=20

def recharge(eng, php):
    if eng >= 75:
        print("You seriously need to reevaluate your life choices")
    else:
        rasp3 = int(input("You could use some rest\n Water (1)          D4C(2)\n: "))
        if rasp3 == 1:
            print("your inner plankton thanks you")
            eng+= 50
        elif rasp3 == 2:
            print("why not replace youself with another one of yourself from an alternate world that isn't exactly an alternate world, and you tehnicaly don't replace yourself, but another self-conscious variant of yourself takes your abilities that he actually never had, but knows how to use in order to achieve the goal he always knew you had, despite him coming from a timeline in which few details are different including said goal. Once you switch, you replace the you from the other world, who becomes the main you, and if in critical condition you may die in his former world, thereby losing the battle held there just because of your selfish desire of achieving the victory that is not actually guaranteed, but tehnicaly speaking, considering that there is an infinite number of yous, is guaranteed, but not for you, but for you,which is quite literaly contradicted by the nature of your abillity. Anyway, now you are in condition to fight and you know what? your hp got maxed out as well. Though right now you are bamboozled, which means that your energy is depleted, but you gained your energy back just because that is what your ability does")
            eng = 100
            php = 100

while bhp:
    if eng == 0:
        print("You are left with nothing but to rest. You fought well, now take yout time before going back in...")
        recharge(eng, php)
    action = int(input("You see yourself facing the boss. What will you choose to do? \n1. Take a step forward, and Attack \n2. Make some distance and Heal \n3. Reevaluate your life decisions and Recharge \n: "))
    if action > 3 or action < 1:
        print("You dont have the power. Try again: ")
    elif action == 1:
        attack(eng, bhp, OHKO)
    elif action == 2:
        heal(php, eng, OHKO)
    elif action == 3:
        recharge(eng, php)

print("WOOO!!! You beat the BOSS finished on the 2nd place. Dont ask why and how you finished on the 2nd place. I dont have enough time to explain that")
