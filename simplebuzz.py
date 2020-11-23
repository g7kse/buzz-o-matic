#A short script that picks a business buzzword randomly from a text file of absurd phrases to be slipped into everyday conversation like you know what it means.

import random

#Open text file list.txt where all the daft buzzwords are there
with open("list.txt", "r") as f: 
    lines = f.readlines()

#print out random line
print (random.choice(lines))
