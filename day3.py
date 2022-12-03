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

for j in range(97,123):  # appends lowercase alphabet to dictionary
    priorities[chr(j)] = (int(j - 96))


for k in range(65,91):  # appends uppercase alphabet to dictionary 
    priorities[chr(k)] = (int(k - 38))

# Checks that dictionary is correct
# print(priorities) 


if Debug: # False for Part II

    for line in lines:
        line.strip()
        split_rucksack = int(len(line) / 2)
        compartment_1 = line[0:split_rucksack]  # split string into two rucksacks 
        compartment_2 = line[split_rucksack::]  
        for letter in compartment_1:  
            if letter in compartment_2:  # checks for duplicate
                priority_score += priorities[letter] # add priority value
                break  # break when duplicate is found so no double counting occurs

    
    print(priority_score)

    
else:  # Part II

    list_of_3 = []
    badge_score = 0
    for line in lines:
        line = line.replace('\n', '')
        if len(list_of_3) == 3:
            for letter in list_of_3[0]:
                if letter in list_of_3[1]:
                    if letter in list_of_3[2]:
                        badge_score = priorities[letter]
                        
            list_of_3 = []
        else: 
            list_of_3.append(line)

    print(badge_score)

            

