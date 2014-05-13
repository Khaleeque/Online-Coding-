from math import sqrt

a = int(sqrt(10203040506070809)/10)
b = int(sqrt(19293949596979899)/10) + 1


def is_type(n):
    k = str(n)[::2]
    if k == '123456789':
        return True
    return False
    
    

for i in range(a,b):

    n = i*10 + 3
    if is_type(n*n):
        break

    n = n+4
    if is_type(n*n):
        break

print n*10
