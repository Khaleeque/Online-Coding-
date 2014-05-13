# Enter your code here. Read input from STDIN. Print output to STDOUT

t = input()


for i in xrange(t):
    n = input()
    
    
    shr = map(int,raw_input().split())
    #shr = [5,7,5,7]#,7,5,2,8,3,6,9,1,4,2,4,3,6,6,4,8,1,2,3,4,3,2,1]
    

    ans  = 0
    locmax = shr[n-1]
    
    for i in range(n-2,-1,-1):
        if shr[i] < locmax:
            ans += locmax - shr[i]
        else:
            locmax = shr[i]
    print ans
        
    


    
    
    
    
    
