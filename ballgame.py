import random

ball = []
number = []
num = []

print('input nums (5 numbers)')
players_numbers = []
for num in range(5):
    num2 = int(input('chosen numbers 1-69: '))
    players_numbers.append(num2)

    ball = list(range(1, 70))

for drawn_number in range(5):
    choseball = random.choice(ball)
    ball.remove(choseball)  
    number.append(choseball)  
    print('number drawn: ', choseball)

print('win num: ', number)
print('your num: ', players_numbers)

if set(number) == set(players_numbers):
    print('winna winna chicken dinna')
ball.clear()
number.clear()
