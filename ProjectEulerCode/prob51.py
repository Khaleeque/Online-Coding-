from prime_check import isprime
from string import maketrans


list_of_primes = []

for i in range(49999,499999):
    j = 2*i + 1
    sj = str(j)
    f = False
    if sj.count('0') == 3:
        f = True
    elif sj.count('1') == 3:
        if sj[5:] != '1':
            f = True
    elif sj.count('2') == 3:
        f = True
    else:
        f = False
        

    if f == True:
        if isprime(j) :
            list_of_primes.append(j)
        
    
for num in list_of_primes:
    snum = str(num)
    if snum.count('0') == 3:
        count = 0
        for i in range(10):
            lk = snum.translate(maketrans("0",str(i) ))
            
            if isprime(int(lk)):
                count += 1
                if count == 8 :
                    print snum
    if snum.count('1') == 3:
        count = 0
        for i in range(10):
            lk = snum.translate(maketrans("1",str(i) ))
            if isprime(int(lk)):
                if int(lk) >99999:
                       count += 1
                if count == 8 :
                    print snum
    if snum.count('2') == 3:
        count = 0
        for i in range(10):
            lk = snum.translate(maketrans("2",str(i) ))
            if isprime(int(lk)):
                if int(lk) > 99999:
                       count += 1
                
                if count == 8 :
                    print '2kl',
                    print snum
        
#l = len(list_of_primes)
#for i in range(10):
#    print list_of_primes[i]
#print l

print 'end'
    

            


