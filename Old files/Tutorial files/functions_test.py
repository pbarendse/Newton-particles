# functions_test.py

# write a function that as an input takes a list of floats x=[x1,x2,x2,...]
# For some mathematical function f(x), for example, f(x)=sin(x),
# as a return value, the function should also give a list [[x1,f(x1)],[x2,f(x2)],....]
# next you iterate over the list items and print:
# "x   f"
# "x1  f(x1) "
# "x2  f(x2) "
# etc

import math

x = [24,123,425,1432,74,234,63]

def function(x):
    lista = []
    for i in x:
        j = math.sin(i)
        lista.append([i,j])
    return lista

def printfunction(x):
    for item in function(x):
        print item

