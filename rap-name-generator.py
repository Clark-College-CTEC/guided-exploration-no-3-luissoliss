# Guided Exploration No. 3
# Luis Solis

import random

possible_names = []

outputFile = open('rap-names-output.txt', 'w')

with open('rap-names.txt', 'r') as dataFile:
    for name in dataFile:
        possible_names.append(name.rstrip())
count = int(input('How many rap names would you like to create? '))
parts = int(input('How many parts should the name contain? '))
for i in range(count):
    name_parts = []
    for j in range(parts):
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])
    outputFile.write(f"{' '.join(name_parts)}\n")
    print(f"{' '.join(name_parts)}")


outputFile.close()
