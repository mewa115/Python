m = str()
m = 'ABC'
for letter in m:
    print('letter is --->', letter)
print('m is -->', m)

x = list()
x.append('1')
x.append('a')
print('x is a list and it is -->', x)

y = dict()
y['name'] = 'Nik'
y['age'] = '26'
print('y is -->', y)

z = tuple()
z = ('Nik', 'Alex', 'Bob')
for name in z:
    print('the name in the tuple is -->', name)
print('z is a tuple and it is -->', z)

(d, f) = (4, 1)
q = (d, f)
print(type(q), q)

x.append(z)
print(x)
x.append(y)
print(x)

x[0] = 3
print(x)

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days[2])

c = {'a': 10, 'b': 1, 'c': 22}
for k, v in c.items():
    print(v, k)

refined = list()
zz = [2, 34, 5, [3, 4]]
for elem in range(len(zz)):
    print(zz[elem])
    refined.append(zz[elem])
print(refined)


yy = dict()
yy['element1'] = 21
yy['element2'] = 22
mmm = yy.keys()
nnn = yy.values()
gg = yy.items()
zzz = yy.get('element3', 0)
print('zzz is', zzz)
for k in yy:
    print(k, ':', yy[k])
for b, c in yy.items():
    print('the pair key-value is:', b, '-', c)
print('mmm is', mmm)
print('nnn is', nnn)
print('the list of yy is', list(yy))
print('gg is is tuple and it is --->', gg)


dd = 0
vv = input('Define the v:')
print('type of the v after input --->', type(vv))

def my_function(vv):
    vv = int(vv)
    print('type of the v in the func --->', type(vv))
    dd = 5 * vv
    return dd

print('type of the v before  the func  invoke --->', type(vv))
dd = my_function(vv)
print('type of the v after invoke --->', type(vv))
print(dd)

