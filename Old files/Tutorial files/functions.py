#functions.py

# Making reliable and understandable software is all about
# structuring computer programs. At the lowest level, one can define small
# blocks of code that (optionally) take an input, do something, and then
# (optionally) produce some output. Such blocks of code are called functions.
# Here we see how to define them in Python

import math

# example function definition:
def first_function(x,y,z):
    return [x,y,z] # this is the return value

a = 4
b = False
c = "Boe"
d = first_function(a,b,c)
print "argument a = ",a
print "argument b = ",b
print "argument c = ",c
print "output d = first_function(a,b,c) = ",d

# for the excercise in functions_test.py you will also need what is
# called list comprehension (Python tutorial 5.1.4), which is a
# quick way of making lists:
n = [i*0.1 for i in range(20)]
print "list of floats made with list comprehension: "
print n

# you may also need functions from the math module of python,
# see its documentation online. If we want to use it, we need to include
# "import math" at the start of the program
x = 0.124
print "example of using function sqrt from the math module"
print "x = ",x
print "math.sqrt(x) = ", math.sqrt(x)
