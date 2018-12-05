import timeit
print(timeit.timeit('''def GCD2(x,y):
    if x > y: 
        small = y 
    else: 
        small = x 
    for i in range(1, small+1): 
        if((x % i == 0) and (y % i == 0)): 
            gcd = i 
              
    return gcd''', number=1000))
