a = ['Bob', 'Ken', 'Sam']    # list of names
for b in a:   # for each name in the list set to variable b and make a print
    print('Hello', b)

##############

a = ['Bob', 'Ken', 'Sam']    # list of names
for b in max(a):   # for each name in the list set to variable b and make a print
    print('Hello', b)

##############

l = -1
print('before', l)
for n in [9, 41, 12, 3, 74, 15]:
    if n > l:
        l = n
    print(l, n)
print('after', l)

#counters

z = 0
for t in [9, 41, 12, 3, 74, 15]:
    z = z + 1
print('z =', z)

