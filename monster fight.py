import random
import time
turn = 1
health = 100
curDamage = random.randint(5, 20) 
smallmodifier = 0

while health > 0:
    health -= curDamage * smallmodifier
    if health <= 0:
        print("you win, you also dealt", int(health), "more damage than you should of. not a bad thing, good job!")
        break
    print("Turn: ", turn, "\nDamage Dealt! \namount:  ", int(curDamage), "\nHealth left: ", int(health))
    time.sleep(1)
    curDamage = random.randint(5, 20) 
    smallmodifier += 0.4
    turn += 1
