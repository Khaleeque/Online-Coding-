
for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            if a != c:
                num1 = a*10 + b

                num2 = b*10 + c
                
                
                f1 = float(num1)/a
                f2 = float(num2)/c


                if f1 == f2 :
                    print a,
                    print " ",
                    print b,
                    print " ",
                    print c,
                    print ""

                num1 = b*10 + a

                num2 = c*10 + a
                
                
                f1 = float(num1)/a
                f2 = float(num2)/c


                if f1 == f2 :
                    print a,
                    print " ",
                    print b,
                    print " ",
                    print c,
                    print ""

            
print 'end'




""""
 ================================
>>> 
1   6   4 
1   9   5 
2   6   5 
4   9   8 
5   7   1 
6   9   1 
end
>>> 

16/64
19/95
26/65
49/98
...
1/4
1/5
2/5
1/2


"""""
















