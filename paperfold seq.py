from datetime import datetime
import tracemalloc


def pfsiterator():
    F = [1]
    i = 0
    while True:
        if i+1 > len(F): F = F + [1] + [(i+1)%2 for i in F][::-1]
        yield F[i]
        i += 1



F = pfsiterator()
for n in range(20):
    print(next(F))
    input()
