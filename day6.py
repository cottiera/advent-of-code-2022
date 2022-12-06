"""

Advent of Code, Day 6!
Alastair Cottier
December 6, 2022

"""

with open("advent_day_6.txt", "r") as inp_txt:
    inp_str = inp_txt.read().replace('\n', '')


mssg_length = 4
PartII = True  # set to False for Part I output
if PartII:
    mssg_length += 10
mssg = []
Flag = False


for n in range(len(inp_str)):
    if Flag:  # final value has been printed
        break
    if len(mssg) != mssg_length:  # mssg_length = 4 for PTI and = 14 for PTII
        mssg.append(inp_str[n])  # fill the list initially
        continue
    else:
        for letter in mssg: 
            check = mssg[:]  # make copy of list named "check"
            check.pop(mssg.index(letter))  # pop first instance of each letter
            if letter in check:  # there exists a duplicate
                # the following two lines shifts the list we are inspecting for duplicates
                # "down" the input string by one character
                mssg = mssg[1:mssg_length]
                mssg.append(inp_str[n])
                break
            elif letter not in check and letter == mssg[-1]:
                # True if entire array has been checked for duplicates and none were found
                print(n)
                Flag = True  # break condition
            else:
                continue



