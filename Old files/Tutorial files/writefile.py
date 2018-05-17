import math

# typeconversion_writefile.py
#
# conversion functions str(), float(), int(),
# file objects, writing files

# sometimes you need to convert one data type to another
# For example, for printing, you may want to convert something to a string,
# or when reading from a file (which typically gives strings) you may want to
# convert these to a float or an int. For this we have the conversion functions
# str(), int(), float(). Examples:

a = 2.1244
str_a = str(a)
print "a = ",a
print "str_a = ",str_a

# you can use str_a to have more control over formatting. 
# this type of string manipulations is also useful when saving data
# (as strings) to files:
str_b = "the value of a is "+str_a+" and that's it."
print "str_b = ", str_b

# file objects, writing files
# first define a file name
filename = "myfile.txt"

# open a python "filehandle" for writing (whence the "w")
f = open(filename,'w')
# write something
f.write("booh \n") # the \n means: new line
f.write("1,2,3\n")
#close filehandle
f.close()
print "data written to file ", filename
