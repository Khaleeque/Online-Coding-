from prime_check import isprime
prim_list = []

for i in xrange(100):
    if isprime(i):
        prim_list += [i]

print prim_list




count = 1
prod = 1

while (prod <= 1000000):
    prod = 1
    for i in xrange(count):
        prod *= prim_list[i]
    count +=1
    
print prod
print count


prod = 1    
for i in xrange(7):
    prod *= prim_list[i]
print prod

#Dekh lena yaar
#I checked with 7 & 8
