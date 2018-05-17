import math

# readfile.py
# conversion functions float(), int(),
# file objects, reading files

filename = "data.csv"
# this is the file name of the file we want to read
# for the present example this should be a .csv file with two columns.
#  You can make one in excel, or simply in notepad,
# it should have this structure:
# 0.123,    65.124
# 23.234,   346.2345
# 12.25,    35.56
# ...

# open a python "filehandle" for reading (whence the "r")
# we are going to read all the lines of the file at once.
# You can also do it line by line, see Python documentation
f = open(filename,'r')
filedata = f.readlines()
f.close()
print "filedata = ",filedata
# filedata is a list, each item of the list is a string
# this may still show some "escape sequences" such as \t (tab) or \n (newline)
# now lets extract the data and put it in a list
# we do this line by line, and split each line at the comma's:

data = [] # list in which we want to put the data (floats !)
for line in filedata:
    splitline = line.split(",")
    print "splitline  = ",splitline
    print "len(splitline) = ",len(splitline)
    # we expect the length to be 2...we want to interpret each item as an integer
    item = [ float(splitline[0]), float(splitline[1]) ] #item is a list with 2 elements
    print "item = ", item
    print "==="
    # now add data to list
    data.append(item) # so this is a list of a list

print "data = ",data    
#accessing the data
# the first index refers to the rows number in the file
# the second index refers to the column number (so it is 0 or 1)
print "data[2] = ",data[2]
print "data[2][1] = ",data[2][1]

