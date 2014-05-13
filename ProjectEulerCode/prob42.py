import math

lisst = []

#Reading File input
with open("prob42_input.txt",'rt') as f:
    for line in f:
        lisst =  line.strip().split('","')
        lisst[0] = lisst[0].translate(None,"\"")
        lisst[len(lisst) - 1] = lisst[len(lisst) - 1].translate(None,"\"")

count  = 0

length = len(lisst)
print length

for i in range(0,length):
    val = 0
    for c in lisst[i]:
        val += ord(c) - 64
    temp = (  math.sqrt(8*val + 1) - 1)/2

    if temp == int(temp):
        count += 1
print count
