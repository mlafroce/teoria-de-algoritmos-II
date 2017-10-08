#!/usr/bin/env python3
import dc3
import sys

myDc3 = dc3.Dc3()

if len(sys.argv) < 2:
	print("Debe proveer un nombre de archivo")
	exit(1)

filepath = sys.argv[1]

with open(filepath, 'r') as content_file:
    content = content_file.read()

procesed = myDc3.process(content)

print ("Processed: {}".format(myDc3.indexes))

#for i, idx in enumerate(myDc3.indexes):
#	print ("{}) {}".format(i, content[idx:]))

print("Done")
