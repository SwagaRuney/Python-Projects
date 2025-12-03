file = open("ex.exe", "w")

for i in range(1, 1001, 1):
    #file.write(f" {i + 1}" + "\n")
    if i % 100 == 0 and i != 0:
        file.write("ok")
    else:
        file.write(str(i))
    file.write("\n")



file.close()
