import time

repeat = True

while repeat:
    age_input = input('Type your age!: ')
    try:
        age = int(age_input)
        print('Thanks! You entered age:', age)
        repeat = False
        if age >=1
    except ValueError:
        print('That isn’t right, please try again.')
