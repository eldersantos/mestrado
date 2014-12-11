''' tuples '''
import math

t = ("First Element", 2, 3.14, (1,'Nested Yeah',3))
'''print("First item: ", t[0])
print("Second item: ", t[1])
print("Thirth item: ", t[2])
print("Nested item: ", t[3][1])
print('The last element of a tuple = {0}'.format(t[-1]))
'''
s = ''.join(['Elder', 'Santos', 'Foda'])
#print(s)

'''
h = ()
print(type(h))
print(len(h))
h = 9, 15
print(type(h))
print(2 in t)
'''

p = s.partition('Santos')
#print(p)

#f = 'The age og {0} is {1} that is really {1}'.format('Elder', 31)
#print(f)
#g = 'The values of the first tuple is one={t[0]} two={t[1]} and three={t[2]}'.format(t=t)
#print(g)
#print('Math contants pi({m.pi:.2f}) and e=({m.e:.4f})'.format(m=math))
print('We can add more items to a tuple, first we need to convert a tuple into a list')
l = list(t)
print(l)
print('Now we can add a new item')
l.append('New item')
print(l[-1])
print('Now convert the list into a tuple again')
t = tuple(l)
print(t)

d = {'a' : [1,2], 'b' : [2,1], 'c' : [2,3]}
print('Dictionary {0}'.format(d))
print(d['a'])
print('Adding a new dic item')
d['d'] = [3,2]
print('Dictionary {0}'.format(d))


