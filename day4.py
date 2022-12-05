"""

Advent of Code, Day 4!
Alastair Cottier
December 4, 2022

"""

inp_txt = open("advent_day_4.txt", "r")
lines = inp_txt.readlines()
overlaps = 0


for line in lines:
    range_one = ''
    range_two = ''
    toggle = False
    

    for letter in line:  # loop creates two strings, range_one and range_two, for each elf
        if letter == ",":
            toggle = True
            continue
        if not toggle:
            range_one += letter
        elif toggle:
            range_two += letter
   

    # create indecies that allow the separaton of the first and last number of each range
    seperator_one = range_one.index('-')
    seperator_two = range_two.index('-')

    # PART I
    """
    # check if second range is within first
    if int(range_two[:seperator_two]) <= int(range_one[:seperator_one]) and \
            int(range_two[seperator_two + 1:]) >= int(range_one[seperator_one + 1:]):
                overlaps += 1

    # check if first range is within the second
    elif int(range_one[:seperator_one]) <= int(range_two[:seperator_two]) and \
            int(range_one[seperator_one + 1:]) >= int(range_two[seperator_two + 1:]):
                overlaps += 1
    else:
        continue
    """

    # PART II
    if int(range_one[:seperator_one]) <= int(range_two[:seperator_two]) and \
            int(range_one[seperator_one + 1:]) >= int(range_two[:seperator_two]):  #  check if first range overlaps 
                                                                                   #  the second
                overlaps += 1

    elif int(range_two[:seperator_two]) <= int(range_one[:seperator_one]) and \
            int(range_two[seperator_two + 1:]) >= int(range_one[:seperator_one]):  # check if second range overlaps
                                                                                   # the first
                overlaps += 1

print(overlaps)



