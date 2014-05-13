max_sum = 0

for i in range(2,100):
    for j in range(2,100):
        num = i**j
        sum = 0
        s = str(num)
        for c in s:
            sum = sum + int(c)
        if sum > max_sum :
            max_sum = sum
    
        
print max_sum  

        
  
