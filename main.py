from os import system

#functiile vor veni aici undeva---
#momentan sunt marcate ca comment ca sa dea run programul. ramane de vaut cand le implantam

#---

bhp = 100
php = 100
eng = 100
clear = lambda: os.system('cls') #curata consola
                                 #nu merge. stiam ca merge. pacat

while bhp:
    print("You have ", php, " HP. The Boss is right before your eyes. What will you do? \n 1. Attack \n 2. Heal \n 3. Recharge your energy")
    x = int(input("Take yout time and choose: "))
    if x == 1:
        #attack()
        continue
    elif x == 2:
        #heal()
        continue
    elif x == 3:
        #recharge()
        continue
    else:
        #clear()
        print("There is no ", x, " option. Don't try to trick me! \n")
