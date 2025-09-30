print("Paste your paper below. Type 'END' on a new line when you're done:")

lines = []
while True:
    line = input()
    if line == "END":
        break
    lines.append(line)

paper = "\n".join(lines)
amount = len(paper)
print("The number of characters is:", amount)
