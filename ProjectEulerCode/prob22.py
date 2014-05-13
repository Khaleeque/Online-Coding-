#Reading File Input
lisst = []
with open("prob22_input.txt",'rt') as f:
    for line in f:
        lisst =  line.strip().split('","')
        lisst[0] = lisst[0].translate(None,"\"")
        lisst[len(lisst) - 1] = lisst[len(lisst) - 1].translate(None,"\"")


lisst = sorted(lisst)

length = len(lisst) + 1#adjustment for loop

sum = 0
for i in range(1,length):
    val = 0
    for c in lisst[i-1]:
        val += ord(c) - 64        
    sum += i*val
print sum    
        
    
