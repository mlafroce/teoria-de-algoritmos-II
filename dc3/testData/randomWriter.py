import sys
from random import randint

if len(sys.argv) < 2:
    print("Debe proveer un nombre de archivo")
    exit(1)

filepath = sys.argv[1]

randomfile = open(filepath, "w" )

for i in range(int(input('How many random numbers?: '))):
    line = str(randint(0, 9))
    randomfile.write(line)

randomfile.close()
