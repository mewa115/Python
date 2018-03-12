#   astr = x
#   istr = y

x = 'Hello Bob'
try:
    y = int(x) # if this statement fails than the program will go to except. It should fails as it not possible to make int variable from string (text)
except:
    y = -1
print('First', y)

x = '123'
try:
    y = int(x) # if this statement fails than the program will go to except. It should not fail as it possible to make int variable from int (numbers)
except:
    y = -1
print('Second', y)


#############################################################


z = input('Enter the number')
try:
    t = int(z)
except:
    t = -1
if t > 0:
    print('Ok. Can proceed')
else:
    print('Enter a number please')
