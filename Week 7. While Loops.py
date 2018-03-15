#### In order go to while function, the statement after the while should be true
n = 5
while n > 0:
    print(n)
    n = n - 1
print(n)


############
# Never get to this loop as if false from the beginning.

n = 0
while n > 0:
    print(n)
print('Done')

##############
# Infinite loop. While is always true and never get off the loop
n = 6
x = 0
while n > 5:
    x = x + 1
    if x < 6:
        continue # skips to the top of the loop
    if x > 7:
        break  ## break is needed so that to get out of the infinite loop or get out of loop after the first attempt
print(x)
print('Done')


