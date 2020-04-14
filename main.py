#!/usr/bin/env python

# Imports
import re
import json

## CONFIGURATION
## Change these variables to configure the program
FILENAME = "My Clippings.txt"
CLIPPING_END_STRING = "=========="

# Global Variables
fileDir = "./" # End with a /
lines = []

# Open the file, read the data line by line into a list
file = open(fileDir + FILENAME, "r")
lines = file.readlines()
file.close()

# Parsing text
curLine = 0
startLine = 0
stopLine = 0

count = 0

def parseBlock(startLine, stopLine):
   # line 1: BOOK_NAME (AUTHOR_NAME)
   line2 = lines[startLine].strip()
   pattern = re.compile(r"([\s\S]+)\(([\s\S]+)\)")
   result = pattern.match(line2)
   book = {}
   if result != None:
       book['name'] = result.group(1).strip()
       book['author'] = result.group(2).strip()
#      print(result.group(1), result.group(2), sep='\t')

   line2 = lines[startLine+1].strip()
   book['posInfo'] = line2
   pattern = re.compile(r"- Your (Highlight|Note|Bookmark) (on|at) (location|page) (\d+)(-?)(\d*) \|? (location (\d+)(-?)(\d*))? ?\|? ?Added on ([a-zA-Z]{3,6}day), (\d{1,2}) ([a-zA-Z]+) (\d{4}) (\d\d):(\d\d):(\d\d)")
   result = pattern.match(line2)
   # \| Added on (\s{3,6}day), (\d{1,2}) (\d{4}) (\d\d):(\d\d):(\d\d)")
   if result != None:
       print(result.groups())
   # line 3: highlight
   line2 = lines[startLine + 3].strip()
   book['highlight'] = line2

#  print(book)

for index, line in enumerate(lines):
#   print("{}: {}".format(index, line))
    if line.rstrip() == CLIPPING_END_STRING:
        count = count + 1
        print(count)
        stopLine = index
        parseBlock(startLine, stopLine)
        startLine = stopLine + 1

