gnum = 1
max_count = 1

for num in  range(837799 ,837899 ):
        count = 1
        knum = num
        while( num != 1):
                if( not num & 1):
                        num = num/2
                else:
                        num = 3*num + 1
                count += 1        
        if (max_count < count ):
                gnum = knum
                max_count = count                
                
print max_count
print gnum


        


                
                
        
