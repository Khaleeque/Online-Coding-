def isBouncy(n):
    s_n = str(n)
    l_n = len(s_n)
    
    inc = True
    dec = True

    count = l_n - 1
    while inc:
        if count == 0:
            break
        if int(s_n[count]) >= int(s_n[count-1]):
            inc = False
    if inc :
        return False
    
    count = l_n - 1
    while dec:
        if count == 0:
            break
        if int(s_n[count]) <= int(s_n[count-1]):
            dec = False
    if dec :
        return False
    else:
        return True

    
