
sum = 0

for a in range(0,10):
    for b in range(0,10):
        for c in range(0,10):
            for d in range(0,10):
                for e in range(0,10):
                    for f in range(0,10):
                        if  100000*f + 10000*a + 1000*b + 100*c + 10*d + e == a**5 + b**5 + c**5 + d**5 + e**5 +f**5:
                            sum += 100000*f +10000*a + 1000*b + 100*c + 10*d + e                        
                            print 100000*f +10000*a + 1000*b + 100*c + 10*d + e

print (sum - 1) #adjustment for 1 as it's not a sum

