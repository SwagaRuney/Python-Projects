import random

temps = [20, 48, 45, 10, -2,]
precip = ["2 inches", "3 inches", "4 inches", "0 inches"]

for i in range(6):
    print(f"Day {i + 1}: ", random.choice(temps), " - ", f"Precipitation: ", random.choice(precip))
