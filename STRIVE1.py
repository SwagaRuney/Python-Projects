import string
import random

#dump
message = []
#dump

string.ascii_lowercase
space = " "
secret_code = [9, 0, 1, 13, 0, 2, 1, 20, 13, 1, 14]

for i in secret_code:
    if i == 0:
        message.append(space)
    else:
        message.append(chr(i + 64))
    #print(string.ascii_lowercase[i])
print(message)
