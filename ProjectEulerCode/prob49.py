# prime numbers are only divisible by unity and themselves
# (1 is not considered a prime number by convention)
def isprime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True
# test ...

import itertools

def ret_num(a):
    return a[0]*1000+a[1]*100+a[2]*10+a[3]*1
    


for a in range(1,6):
    for b in range(0,10):
        for c in range(0,10):
            for d in range(0,10):
                li = [a,b,c,d]                
                k = list(itertools.permutations(li, 4))
                k = map(ret_num,k)                            
                k = list(set(k))                
                k = filter(isprime, k )            
                #print k

                if len(k) > 2:
                    #thre = list(itertools.permutations(k, 3))
                    thre = list(itertools.combinations( k, 3))
                    for i in range(0,len(thre)):
                                   if 2*thre[i][1] == thre[i][0] + thre[i][2]:
                                       st =  str(thre[i][0]) +str(thre[i][1]) + str(thre[i][2])
                                       if len(st) == 12 :
                                           print st
                                           



print 'end'

#############W#O#R#K#I#N#G#

