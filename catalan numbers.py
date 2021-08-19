from math import factorial, log10

def catalan(n):
    return factorial(2*n)//(factorial(n) * factorial(n+1))
