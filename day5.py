"""

Advent of Code, Day 5!
Alastair Cottier
December 5, 2022

"""
inp_txt = open("advent_day_5.txt", "r")
lines = inp_txt.readlines()
my_dict = {}
for j in range(10):
    my_dict[j] = []

for line in lines:
    line.strip()
    count = 1
    length = len(line)
    if line[1].isnumeric():
        break
    for i in range(1,length,4):
        if line[i] != ' ':
            my_dict[count] += line[i]
            count += 1
        else:
            count += 1


for m in range(10):
    my_dict[m] = list(my_dict[m])
    my_dict[m].reverse()

for line in lines:
    line.strip()
    line = line.split()
    amnt = 0
    if len(line) == 0 or line[0] != 'move':
        continue
    else:
        for letter in line:
            if letter.isalpha():
                line.remove(letter)
            else: 
                continue

    print(line)
    """
    print(line)
    if len(line) == 4:
        amnt = 1
    if len(line) == 3:
        amnt = 0
    """
    # eg.., sequence = 1531
    # 
    # amnt = 1
    # for n in range(15):
    #  my_dict[1] += my_dict[3][last]
    #  my_dict[3][last] = ''

    """
    for n in range(int(line[0])):
        my_dict[int(line[-1])].append(my_dict[int(line[-2])][-1])
        my_dict[int(line[-2])].pop()
        print(my_dict)
    """

    # PART II
    print(my_dict)
    n = int(line[0])
    my_dict[int(line[-1])].append(my_dict[int(line[-2])][-n:])
    my_dict[int(line[-2])] = line[-2][-n:]

for key in my_dict:
    if len(my_dict[key]) != 0:
        print(my_dict[key][-1])


