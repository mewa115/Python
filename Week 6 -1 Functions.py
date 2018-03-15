def x():
    print("Hello")
    print('Fun')
x()
print('Zip')
x()

big = max('Hello world')
print(type(big))
print(big)


###########################
def greet(lang):
    if lang =='es':
        return('Hola')
    elif lang == 'en':
        return('Hello')
print(greet('en'), 'Bob')
print(greet('es'), 'Hulo')


####################
def greet():
    return 'Hello'
print(greet(),'Sally')

##################

import romeo


##########################

def sumfunction(a,b):
    added = a + b
    return added
x = sumfunction(3,5)
print (x)


###########################


def thing():
    print('Hello')

print('There')


###########

def func(x) :
    print(x)

func(10)
func(20)

###############

def stuff():
    print('Hello')
    return
    print('World')

stuff()

##############

def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('fr'),'Michael')



######################

def addtwo(a, b):
    added = a + b
    return a

x = addtwo(2, 7)
print(x)