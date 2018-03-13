s = input("Enter Score: ")
s = float(s)
if s < 0:
    print('Put correct grade between 0 and 1')
elif s < 0.6:
    print('F')
elif s < 0.7:
    print('D')
elif s < 0.8:
    print('C')
elif s < 0.9:
    print('B')
elif s <= 1:
    print('A')
else:
    print('Put correct grade between 0 and 1')