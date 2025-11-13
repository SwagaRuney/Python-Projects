games = [
    "Super Mario Bros.",
    "Pac-Man",
    "Tetris",
    "The Legend of Zelda",
    "Donkey Kong"
    ]

index = int(input("Enter a Number between 0-4: ",))

if 0 <= index < len(games):
    print("Game picked: ", games[index])
else:
    print("Invalid, please rerun program and choose again.")
