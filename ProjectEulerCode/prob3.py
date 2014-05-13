import math

out = 0
temp = 0
inp = 600851475143 
for i in range(2, int(math.sqrt(inp)), 1):
	if (inp % i == 0):
		temp = 1
		for j in range(int(math.sqrt(inp/i)), 2,-1):
			if ((inp/i) %j == 0):
				temp=0
				break
		if (temp == 1):
			out = inp/i
			break
		else:
			inp = inp / i




num1 = 600851475143 

def IsPrime(n):
    for i in range(2,n):
        if n%i == 0:
            return 0
    return 1


for num in range(2,int(math.sqrt(num1))):
   if num1%num == 0 :
       other_num = num1/num
       if IsPrime(other_num) == 1:
           print other_num
           break
       
