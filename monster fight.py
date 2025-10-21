print('RULES: \n you are up against a wrestler that is deciding to give you free hits because of his ego, \n every time that you attack him, his defense lowers, which will multiply your attack damage, your job is to destroy him. \nDefense: 100\nAttack: 0\n Description: A rude brawler man idk just kill him or something i dunno')

import random
import time
turn = 1
health = 1000
curDamage = random.randint(5, 20) 
smallmodifier = 0


exclaimtable = { "Doesn't even hurt...", "Keep trying! You'll get nowhere!", "pff...", "ow!", "just give up!"}
othersayingstuff = ['says: ', 'exclaims: ', 'quotes: ', 'scoffs: ']
print('PRESS ENTER TO BEGIN THE FIGHT')
input()
print('the battle begins! (press enter to attack)')
while health > 0:
    health -= curDamage * smallmodifier
    input()
    if health <= 0:
        print("The boss screams: AHHHHHH! Curse you . . !\nyou win, you also dealt", int(health), "more damage than you should of. \nThat's not a bad thing, good job!")
        input()
        break
    print("Turn: ", turn, "\nDamage Dealt! \namount:  ", int(curDamage), "\nHealth left: ", int(health))
    print('\nDETAILS : \nThe boss', othersayingstuff[random.randint(0, 3)], random.choice(list(exclaimtable)), '\nYou take another shot . . .\n')
    
    curDamage = random.randint(5, 20) 
    smallmodifier += 0.4
    turn += 1
