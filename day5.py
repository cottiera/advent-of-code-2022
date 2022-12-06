"""

Advent of Code, Day 5!
Alastair Cottier
December 5, 2022

"""

inp_txt = open("advent_day_5.txt", "r")
lines = inp_txt.readlines()
my_dict = {}
for j in range(10):  # preallocate dict keys
    my_dict[j] = []

for line in lines:
    line.strip()  # strip \n
    count = 1
    length = len(line)
    if line[1].isnumeric():  # line with stack labels
        break
    for i in range(1,length,4):  # loop creates stacks of crates as strings in a dictionary 
        if line[i] != ' ':
            my_dict[count] += line[i]  # adds new crate to stack by string concatenation
            count += 1
        else:
            count += 1


for m in range(len(my_dict)):  # loop through dictionary and change crate stacks from strings to lists
    my_dict[m] = list(my_dict[m])
    my_dict[m].reverse()  # reverse list order so last item is top of crate stack 

for line in lines:
    line.strip()
    line = line.split()  # take in lines as lists
    if len(line) == 0 or line[0] != 'move':  # skip over all lines that arent crane instructions
        continue
    else:
        for item in line:
            if item.isalpha():  # remove all words from indiv. instruction so only numeric instructions remain
                line.remove(item)
            else: 
                continue

    # PART I

    # eg.., sequence = 1531
    # 
    # amnt = 1
    # for n in range(15):
    #  my_dict[1] += my_dict[3][last]
    #  my_dict[3][last] = ''

    """
    # moves crates one at a time from giving stack to receiving stack
    # after each transfer, lat item from giving list is popped 
    for n in range(int(line[0])):
        my_dict[int(line[-1])].append(my_dict[int(line[-2])][-1])
        my_dict[int(line[-2])].pop()
        print(my_dict)
    """

    # PART II

    n = int(line[0])
    my_dict[int(line[-1])].extend(my_dict[int(line[-2])][-n:])  # remove spliced list
    for m in range(n):  # remove elements that got moved
        my_dict[int(line[-2])].pop()

for key in my_dict:  # for each stack, stored in my_dict, return the last element (element at top of stack)
    if len(my_dict[key]) != 0:
        print(my_dict[key][-1])


