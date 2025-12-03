import random
import time

bulb = [True, True, True, True, False]

def isWorking(test_bulb):
    print(test_bulb)

for light in bulb:
    isWorking(light)
    time.sleep(.05)
