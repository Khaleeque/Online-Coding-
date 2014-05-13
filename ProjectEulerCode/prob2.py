sum =0

num1 = 1
num2 = 2
num3 = 3

while( num2 <= 4000000):
    sum = sum + num2
    num1 = num2 + num3
    num2 = num3 + num1
    num3 = num1 + num2
    
    

print sum,
