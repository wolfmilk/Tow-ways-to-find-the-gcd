# Use Euclid’s algorithm 
def gcdE(m, n):
    if m % n != 0:
       return gcdE(n, m % n)
    else:
        return n






