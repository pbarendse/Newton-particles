# basics.py
#
# data types: int, float, string
# compound data type: list 
# if, for, while, range, print statements

# variable a holds an integer
a = 4
print "a = ",a
print "a is ",type(a)

# variable b holds a float
b = 6.235
print "b = ",b
print "b is ",type(b)

# variable c holds a string
c = "blabla"
print "c = ",c
print "c is ",type(c)

# we can put them in the list d:
d = [a,b,c]
print "d = ",d
print "d is ",type(d)

#lists have many useful methods, see section 5.1
print "with the append method we can add something at the end of the list d"
print "for example, after doing d.append(300000) we have: "
d.append(300000)
print "d = ", d
print "len(d) = ", len(d)

# we can iterate over the elements of list d using the for construct
# iteration often use the range statement, that makes integer lists:
n = len(d)  # length of the list d
nrange = range(n)
print "n=len(d) = ", n
print "nrange  range(n) = ",range(n)
print "iterate over elements of list d using range:"
for i in range(n):
    print "element ", i , "=", d[i]


# a more succinct way of iterating over a list is
print "iterate over elements of list d without using range:"
for item in d:
    print item

