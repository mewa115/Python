fam = ['nik', 1.80, 'mom', 1.62, 'ler', 1.64, 'dad', 1.75, 'nik', 1.80]
print(fam)

fam1 = [['nik', 1.80],
        ['mom', 1.62],
        ['ler', 1.64],
        ['dad', 1.75]]

print(fam1)

print(type(fam))

familyheight = fam[1] + fam[3] + fam[5] + fam[7]  # sum of height's of all family members
# counting of the elements starts from 0, i.e. 0,1,2,3,4,5... etc.
# Reverse counting starts from

print(familyheight)
print(fam[3])  # show me the element 4 from the list as the counting starts from 0. If I define 3, it means, 0,1,2,3,4, which in fact is forth.
print(fam1[-2])  # show reverse, in case it is easier to count from the end. In this example it shows full sublist
print(fam[-2])  # show reverse, in case it is easier to count from the end. In this example it shows 2 from the end. Counting starts as -1,-2,-3,... etc.
print(fam[4:6])  # show from the list element 4 and 5
print(fam[:2])  # from beginning to 0 to 1
print(fam[4:])  # from 4 till end
print(fam1[-1][1]) # if I want to fetch the value from the sublist


# Manipulate with the values in the list
fam[1] = 1.81  # change the value in the list
print(fam[1])

fam[0:2] = ['nikita', 1.805]  # change several values in the list
print(fam)

fam = fam + ['sosed', 1.90]
print(fam)

# del(fam[-1])   # delete last element
# del(fam[-1])  # delete last element once again
# del (fam[-1]); del (fam[-1])  # separate with semicolon so that to execute more than one command on a single line
del(fam[-2:])  # delete from -2 field till the end
print('Updated list:', fam)

# When you make one list equal to another you basically coping reference to the list but no the values in the list
fam2 = ['yaha', 1.9, 'val', 2.0, 'mar', 1.85, 'svet', 1.8]
fam2 = fam
fam2[1] = 1.92
print(fam2)  # therefore, here not yaha = 1.92 but nikita is 1.92 because nikita in the list of fam

fam2 = list(fam)  # this the copy of the list
fam2 = fam[:]  # this is the copy of the list as well

fam2[1] = 1.79
fam[1] = 1.8

print(fam2)
print(fam)

fam4 = [1.3, 2.05, 1.86, 1.70]
zz = max(fam4)
zz = float(zz)
print(round(zz, 1))

kk = 'what the car?'
print(len(kk))

mm = complex(1/3)
print(mm)

fam5 = sorted(fam4, reverse=True)  # Sorting apply
print(fam5)

# Object has a type. Object 5 has a type str
# Methods are the functions that belong to objects
# Example of methods: str--> capitalize(), replace(), float --> bit_length(), conjugate(), list --> index(), count()
# Specific methods are applied to different types,

fam = fam + ['nik', 1.80]
print(fam)
print(fam.index('ler'))  # fam is an object with the type of list. Index is a method. As a result I will receive an element with index 4
print(fam.count('nik'))  # count how many times I have nik in the list fam

mom = 'svet'
#mom = mom.capitalize()
mom = mom.replace('svet', 'mom')  # method replace replaces svet with mom
mom = mom.capitalize()  # method capitalized makes the first letter capitalized
print(mom)

print(fam)
fam.append('nata')
fam.append(1.65)  #  it adds new value to the list bit it did not.
print(fam)
fam.reverse()  # makes a reverse order for the elements in the list
print(fam)

help(fam.append)  # help function

mom = 'svet'
mom = mom.upper()  # this method makes all characters with capital size.
print(mom)


help(fam.append)


#  Packages is a directory of python scripts
#  pkg/mod.py
#  packages should be installed.
#  additional packages are PIPs


import romeo  # import py file
print(romeo)  # show the path?

# I have downloaded  PIP file from http://pip.readthedocs.io/en/stable/installing/
# after that I executed downloaded .py file with python interpratator
# that gave me an opportunity to import different packages

import numpy
import math  # here is a full import of math package
r = 0.43
C = 2*r*math.pi
A = math.pi*r**2
C = round(C, 2)
A = round(A, 2)
print("Circumference: " + str(C))
print("Area: " + str(A))

# Definition of radius
r = 192500
# Import radians function of math package
from math import radians
# Travel distance of Moon over 12 degrees. Store in dist.
dist = r * radians(12)
# Print out dist
print(dist)

#  There are several ways to import packages and modules into Python. Depending on the import call, you'll have to use different Python code.
#  suppose you want to use the function inv(), which is in the linalg subpackage of the scipy package. You want to be able to use this function as follows:
# I want to import function and name it as my_inv
#  from scipy.linalg import inv as my_inv

print(dist) # test

import numpy as np


np_height = np.array(height)
np_height

np_weight = np.array(weight)
np_weight



