from os import system
from time import sleep
from keyboard import wait

php = 100
bhp = 100
OHKO = 100
eng = 100

def attack():
	global bhp, eng, OHKO  
    rasp1 =int(input("You choose to attack, what will you use? \n-------- \n Made in Heaven (or grateful dead) (1)          Tusk Act 4 (2)"))
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
		
def heal():
	global php, eng, OHKO 
    if php >= 75:
        print("you are determined to continue attacking")
        #aici nu isi da heal, ci trebuie sa aleaga alta actiune
    else:
        rasp2 = int(input("It seems your health bar is pretty low, what will you do? \n Crazy Diamond (1)           Zombie Horse String (2)\n"))
        if rasp2 == 1:
            print(" Dora the Explora\n you recovered all your health points but your hand looks kind of funny now")
            php = 100
            eng-=40
            OHKO -=25
        elif rasp2 == 2:
            print("forgot what the panel said\n magicaly, the wounds you sew dissapeared")
            php += 30
            eng-=20
			
def recharge():
	global eng, php 
    if eng >= 75:
        print("You seriously need to reevaluate your life choices")
    else:
        rasp3 = int(input("You could use some rest\n Water (1)          D4C(2)\n"))
        if rasp3 == 1:
            print("your inner plankton thanks you")
            eng+= 50
        elif rasp3 == 2:
            print("why not replace youself with another one of yourself from an alternate world that isn't exactly an alternate world, and you tehnicaly don't replace yourself, but another self-conscious variant of yourself takes your abilities that he actually never had, but knows how to use in order to achieve the goal he always knew you had, despite him coming from a timeline in which few details are different including said goal. Once you switch, you replace the you from the other world, who becomes the main you, and if in critical condition you may die in his former world, thereby losing the battle held there just because of your selfish desire of achieving the victory that is not actually guaranteed, but tehnicaly speaking, considering that there is an infinite number of yous, is guaranteed, but not for you, but for you,which is quite literaly contradicted by the nature of your abillity. Anyway, now you are in condition to fight and you know what? your hp got maxed out as well. Though right now you are bamboozled, which means that your energy is depleted, but you gained your energy back just because that is what your ability does")
            eng = 100
            php = 100

while bhp and php:
    system('cls')
	print(f"you are currently {100-php} points away from dying - you have {php} hp left")
    if eng == 0:
        print("You dont feel your legs anymore (HaHa). You are left with nothing but to recharge. that and quitting")
        recharge()
    if bhp > 75:
        action = int(input("you see yourself facing the boss. What will you do\n 1. take a step forward and attack\n2. Keep your distance and heal\n3. Take a quick sip and recharge")
        if action > 3 or action < 1:
            print("That's not how it works. Try again: ")
        elif action == 1:
            attack(bhp, php, eng, OHKO)
        elif action == 2:
            heal(php,eng,OHKO)
        elif action == 3:
            recharge(eng,php)
        sleep(2)
        print("<<Thou may think thy power is enough to vanquish any foe thou encounter>>")
        sleep(1)
        print("<<soon thou will realise thy mistake>>")
        php-=13
    elif bhp > 25 and bhp < 75:
        action = int(input("You have angered the boss, and now he deals more damage.\n1. take a step forward an attack\n2. Keep your distance and heal\n. Take a quick sip and recharge")
        if action > 3 or action < 1:
            print("That's not how it works. Try again: ")
        elif action == 1:
            attack(bhp, php, eng, OHKO)
        elif action == 2:
            heal(php,eng,OHKO)
        elif action == 3:
            recharge(eng,php)
        sleep(2)
        print("<<Long have I waited for such a formidable foe>>")
        sleep(1)
        print("<<fear not as your death will be remembered>>")
        if bhp <68 and bhp > 67:
            print ("Oh, the POWER!")
            sleep(1)
            print("THE WORLD")
            sleep(1)
            print("OVER HEAVEN!\n the ability to overwrite reality is now mine") 
            php = 0
            eng = 0
            bhp = 100
        php-=20
    elif bhp <25:
        print("It's do or die\n if you were lucky enough, you might have skipped this stage, but the boss' true powers finnaly awakened")
        if random.choice(1,0) == 1:
            php == 0
        else:
            bhp == 0
	print("press X to continue...")
	wait('x')

if bhp == 0:
    print("WOOO!!! You beat the BOSS, but still finished on the 2nd place. Dont ask why and how")
elif php == 0:
    print("you may win if you try again")
