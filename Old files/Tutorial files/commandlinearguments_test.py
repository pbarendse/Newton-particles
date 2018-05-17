# commandlinearguments_test.py
# write a script that you call from the commandline as
# C:>python.exe commandlinearguments_test.py someinputfilename someoutputfilename
# save the filenames as strings in appropriately named variables 
# and print them as output (eg "infile = someinputfilename" etc)

import sys

arguments = sys.argv
someinputfilename = str(arguments[1])
someoutputfilename = str(arguments[2])

print someinputfilename, 'test', someoutputfilename


