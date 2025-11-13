import time
ELIST = ["Candy","Burger","Pizza","SpringRolls","Chips"] 
run = True

while run:
   
    print("""
    Main Menu

1. Add an item to the list
2. Remove an item from the list
3. View the current list
4. Exit

""")
    c = input("Menu num: ")
    if c == "1":
        item = input("Input item you want to add: ")
        ELIST.append(item)
    elif c == "2":
        item = input("Input item you want to remove: ")
        if item in ELIST:
            ELIST.remove(item)
        else:
            print(f"Invalid \"{item}\" in list of \"{ELIST}\"")
    elif c == "3":
        print(ELIST)
        input("Enter to Continue")
    elif c == "4":
        print("Exiting. . .")
        time.sleep(2)
        run = False
    else:
        print("Invalid option, please pick again.")
        time.sleep(3)
    
