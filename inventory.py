inventory = [
    "Elden Ring",
    "Fortnite",
    "Minecraft",
    "Call of Duty",
    "Spider-Man 2",
    "Fortnite",
    "Hogwarts: Legacy",
    "Zelda: Tears of the Kingdom"
    ]

inventory.remove(inventory[1])
inventory.append("Grand Theft Auto 6")

for i in range(len(inventory)):
    print(inventory[i])
