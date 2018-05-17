#ARGUMENT PASSING FOR SCRIPTS

# the computer simulation scripts that you will use are to be called from the
# msdos commandline, together with some arguments such as eg filenames
# for example: "python myscript.py inp.txt" means that python will
# execute the script "myscript.py", and in the script, we can use
# the commandline argument "inp.txt" (a filename) as a variable
# Here we show how this works

# functions for command line argument handling are
# provided by the standard python module "sys", that we need to import
import sys

# the sys module stores the commandline arguments in the list argv
arguments = sys.argv

print "number of arguments: ", len(arguments) 
for i in range(len(arguments)):
    print "argument ", i , " = ", arguments[i]




