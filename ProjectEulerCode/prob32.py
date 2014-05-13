from pandigital import ispandigital


s = set()

for i in range(1,10000):
    for j in range(1,10000):
        prod = i*j
        str1 = str(i) + str(j) + str(prod)
        if len(str1) == 9 :
            if ispandigital(int(str1)) == True:                
                print str1
                s = s.union([prod])
                k = sum(s)
                

print s
print len(s)
print k

# sum of set([7632, 5346, 5796, 7254, 6952, 7852, 4396])

