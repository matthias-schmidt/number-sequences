def complete(numbers,c):
    n = len(numbers)
    rot = {0:0, 1:1, 6:9, 8:8, 9:6}
    if c == 0: return int(''.join([str(digit) for digit in numbers]+[str(rot[digit]) for digit in numbers[::-1]]))
    else: return int(''.join([str(digit) for digit in numbers[:-1]]+[str(rot[numbers[-1]])]+[str(rot[digit]) for digit in numbers[:-1][::-1]]))

def udn(n):
    nstr = str(n)

    # count upside down numbers with less digits
    ndig = [int(x) for x in str(n)]
    nlen = len(ndig)
    if nlen < 5: shift = [0, 3, 7, 19][nlen-1]
    else: shift = 7+32*sum([5**i for i in range((nlen-1)//2-1)])+((nlen-1)%2)*12*5**((nlen-1)//2-1)

    # count smaller upside down numbers with the same number of digits
    less = [0,1,2,2,2,2,2,3,3,4]
    lessc = [0,1,2,2,2,2,2,2,2,3]
    if nlen == 1: return shift + lessc[ndig[0]]
    count = (less[ndig[0]]-1) * 5**(nlen//2-1) * 3**(nlen%2)
    i = 0
    while i < nlen//2-1 and ndig[i] in [0, 1, 6, 8, 9]:
        i += 1
        count += less[ndig[i]] * 5**(nlen//2-1-i) * 3**(nlen%2)
    if i == nlen//2-1:
        if nlen%2 == 0:
            if ndig[i] in [0, 1, 6, 8, 9] and complete(ndig[:nlen//2],0) < n: count += 1
        else:
            if ndig[i] in [0, 1, 6, 8, 9]:
                count += lessc[ndig[nlen//2]]
                if ndig[nlen//2] in [0, 1, 8] and complete(ndig[:nlen//2+1],1) < n: count += 1
    return shift + count
