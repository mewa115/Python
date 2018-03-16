fam = ['nik', 1.80, 'mom', 1.62, 'ler', 1.64, 'dad', 1.75]
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

del(fam[-1])  # delete last element
del(fam[-1])  # delete last element once again
print(fam)