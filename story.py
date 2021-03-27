from os import system
from time import sleep

while bhp and php:
    system('cls')
    if eng == 0:
        print("you are left with nothing but to recharge. that and quitting")
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
        
    print(f"you are currently {100-php} points away from dying")
if bhp == 0:
    print("WOOO!!! You beat the BOSS, but still finished on the 2nd place. Dont ask why and how")
elif php == 0:
    print("you may win if you try again")
