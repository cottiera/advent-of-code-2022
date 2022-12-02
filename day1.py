"""
Advent of Code 2022, Day 1!
Alastair Cottier
December 1, 2022

"""

text_file = open('advent_day_1.txt', 'r')
lines = text_file.readlines()
cals = 0
elf_totals = []
top3 = 0


for line in lines:
    line.strip()
    if line != '\n':  # still in current elf's bag, add cals
        cals += int(line)
    else:  #new elf, add pprevious elf's total to list 
        elf_totals.append(cals)
        cals = 0  #reset cals forr new elf


elf_totals.sort()  #ascending order
length = len(elf_totals) 
top3_list = elf_totals[length-3:] #splice list for last 3 elfs totals // new list top3_list


for item in top3_list:  #sum top3_list
    top3 += int(item)

print(max(elf_totals))  #highest cals
print(top3)  #to 3 highest cals

