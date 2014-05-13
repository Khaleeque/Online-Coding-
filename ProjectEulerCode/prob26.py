from prime_check import isprime

def lenr(den):
    num = 1
    strr = ''

    for i in range(1,1000):
        while num < den :
            num *= 10
            if num < den:
                strr += '0'

        k = num/den
        num = num%den
    
        strr += str(k)
    #print strr
    s = strr[990:]
    #print s
    k = strr[:990]
    #print k
    l = k.rfind(s)
    print den,
    print 990- l
    
    
prim_list = []    
    
for i in range(23,1000):
    if isprime(i):
        prim_list += [i]


for j in prim_list:
    lenr(j)


#Done this problem in a very dirty way    
        
    
    

