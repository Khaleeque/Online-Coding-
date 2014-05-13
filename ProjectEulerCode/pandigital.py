def ispandigital(x):
    s = set()
    for c in str(x):
        s = s.union([int(c)])    
    if s == set([1,2,3,4,5,6,7,8,9]) :
        return True
    else:
        return False
    


