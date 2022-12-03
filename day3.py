"""

Adventy of Code 2022, Day 3!
Alastair Cottier
December 3, 2022

"""

inp_txt = open("advent_day_3.txt", "r")
lines = inp_txt.readlines()
priorities = {}
priority_score = 0

Debug = False  # Debug to check dictionary execution

for j in range(97,123)
    priorities[chr(j)].append(int(j - 96))


for k in range(65,91):
    priorities[chr(k)].append(int(k - 38))

print(priorities)


if Debug

    for line in lines:
        line.strip()
        split_rucksack = len(line) / 2
        compartment_1 = line[0:split_rucksack]
        compartment_2 = line[split_rucksack + 1:]
        for item in compartment_1:
            if item in compartment_2:
                priority_score += pritorities[item]

    print(priority_score)
