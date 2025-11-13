import random
import sys

candy_bag = []
candy_storage = []
candy = ["smartie","snicker","cliff bar","licorice", "reese cup", "ButterFinger", "Mr. Goodbar", "old nickle", "rock", "vampire teeth", "scented eraser", "kit kat"]
trickortreat = True
while trickortreat:
    print("""
Digital Trick or Treat
        Main Menu
    1. Check candy Storage

    2. Go trick or treating

    3. Dump digital candy back into candy storage

    4. save candy storage to candy file
    
    5. load candy file to candy storage

    6. finsh trick or treating
    
""")
    choice = input("Enter valid menu number: ")

    if choice == "1":
        print(f"Current items in bag: {candy_bag}")
        print(f"Candy Storage: {candy_storage}")
    elif choice == "2":
        print("You go Trick-or-Treating")
        chosen_candy = random.choice(candy)
        print(f"Candy Get: {chosen_candy}")
        candy_bag.append(chosen_candy)
    elif choice == "3":
        candy_storage.extend(candy_bag)
        candy_bag.clear()
        print("Candy moved to storage.")
        print("Candy bag emptied.")
        
    elif choice == "4":
        file = open("candy_file.txt", "a")
        for c in candy_storage:
            #print(c)
            file.write(c + "\n")
        file.close()

    elif choice == "5":
            file = open("candy_file.txt", "r")
            for line in file:
                candy_storage.append(line)
                print(line)
    elif choice == "6":
        sys.exit
    else:
        print("not valid menu option")
