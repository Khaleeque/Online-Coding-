import math

num1 = 100

a = range(101)
b = sum(a)
c = b*b
print c


d = sum([x*x for x in range(0,101)])
print d

f = c - d
print f
