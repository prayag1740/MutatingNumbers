# Copyright 2018, Supragya Raj
# You are free to use and distribute this code under MIT license

import random

# encodings

enclen = 15

print("Mutation of numbers")
print()
tgt = 20 #input("Target number: ")
max_len = 5 #input("Target length: ")
gencnt = 10 #input("Members in each generation: ")
# initial batch of strings

print("Initial batch: ")
members = []
values = []
print("hello")
for x in range(gencnt):
    string = ""
    len = random.randrange(0,max_len)
    if(len%2 == 0):
        len += 1
    for y in range(len):
        if(y%2 == 0):
            encode = random.randrange(0,10)
        else:
            encode = random.randrange(11,15)
        if(encode == 11):
            string += "+"
        elif(encode == 12):
            string += "-"
        elif(encode == 13):
            string += "*"
        elif(encode == 14):
            string += "/"
        else:
            string += str(encode)
    members.append(string)
    try:
        values.append(eval(string))
    except ZeroDivisionError:
        values.append(-3000)
print(members)
print(values)

