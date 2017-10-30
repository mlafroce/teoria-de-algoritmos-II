#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dc3c as dc3
import search
import sys
import struct

myDc3 = dc3.Dc3()

if len(sys.argv) < 2:
	print("Debe proveer un nombre de archivo")
	exit(1)

pattern = "hola"

if len(sys.argv) == 3:
	pattern = sys.argv[2]

filepath = sys.argv[1]

with open(filepath, 'r') as content_file:
    content = content_file.read()

procesed = myDc3.process(content)

#print ("Processed: {}".format(myDc3.indexes))

#searcher = search.Search(myDc3.indexes, content)

#with open("indexes.idx", 'wb') as indexFile:
#	for idx in myDc3.indexes:
#		indexFile.write(struct.pack('i', idx))

# for i, idx in enumerate(myDc3.indexes):
#	print ("{}) {}".format(i, content[idx:]))

#indexRange = searcher.search(pattern)

#print("Encontrado entre los rangos {}".format(indexRange))
#print(myDc3.indexes[indexRange[0] : indexRange[1]])

print("Done")
