import datetime

curage = 16

current_datetime = datetime.datetime.now()
year = current_datetime.year

target_year_input = input('Enter target year: ')
taryear = int(target_year_input)

yeardiff = taryear - year
agetarget = curage + yeardiff

print("You will be " + str(agetarget) + " years old in the year " + str(taryear) + ".")
