a = 1
b = 1
c = 998

for a in range(1,999):
        for b in range(1,(1000-a)):
                c = 1000 - a - b
                if ( a*a + b*b == c*c):
                        print a,
                        print b,
                        print c,
                        print a*b*c
print "end"                        
