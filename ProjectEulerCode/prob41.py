#There cannot be 1-9 OR 1-6 OR 1-3 pan prime
#
#


import itertools
from prime_check import isprime
"""
perm_list = list(itertools.permutations([1,2,3,4,5,6,7,8]))

lisst = []

for i in perm_list:
    num = ''
    for j in range(0,8):
        num = num + str(i[j])
    if isprime(int(num)):
        lisst.append(num)

print lisst

print 'end'
"""

    
perm_list = list(itertools.permutations([1,2,3,4,5,6,7]))

lisst = []

for i in perm_list:
    num = ''
    for j in range(0,7):
        num = num + str(i[j])
    if isprime(int(num)):
        lisst.append(num)

print lisst[len(lisst) - 1]

print 'end'
