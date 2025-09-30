looping = True
count = 0 
while looping:
    count += 100
    print(count)

    if count == 1000000:
        looping = False
