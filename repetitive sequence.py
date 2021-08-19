from math import log10
from datetime import datetime
import tracemalloc


# semifast:

def repseq1(n):
    F = [0, 1, 2, 2]
    if n < 4: return F[n]
    s, m, k = 3, 5, 3
    while True:
        F.extend([k for ctr in range(F[k])])
        if m + k*F[k] > n: return s + (n-m+F[s+1]-1)//F[s+1]
        s += F[k]
        m += k*F[k]
        k += 1


# fast:
        
def repseq(n):
    if n < 12: return [0, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5][n]
    F = [0, 1, 2, 2]
    step, s, t, u = 3, 3, 5, 11
    while True:
        F.extend([step for i in range(F[step])])
        ss = s + F[step]
        uu = u + step*((ss**2 + ss - s**2 - s)//2)
        if uu > n:
            s += 1
            while True:
                if u + step*s > n: return t + (n-u+s-1)//s
                u += step*s
                t += step
                s += 1
        t += step*F[step]
        step += 1
        s, u = ss, uu

from itertools import count



def repseqF(n):
    F = [0, 1, 2, 2]
    if n < 4: return F[:n]
    s = 3
    m = 5
    k = 3
    while k <= n:
        F.extend([k for ctr in range(F[k])])
        k += 1
    return F
        

n = 2**82


starttime=datetime.now()
#tracemalloc.start()
print(repseq(n))
#print(tracemalloc.get_traced_memory())
#tracemalloc.stop()
print(format(datetime.now()-starttime))

