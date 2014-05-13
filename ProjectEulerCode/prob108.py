primList = [2,3,5,7,11,13,17]

def num_primDivs(n):

    nod = 1
    rem = n

    
    for k in primList:
        
        exp = 1

        if k*k > n :
            return nod*2

        while rem%k == 0:
            exp += 2
            rem = rem/k
        nod *= exp

        if rem == 1:
            return nod

    return nod        
        
n = 1
limit = 1000

while(True):
    if ( (num_primDivs(n) + 1)/2 > limit) :
        print n
        break
    n += 1
    
