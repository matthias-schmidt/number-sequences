def fibmult(a,b):
    return [a[0]*b[0]+a[1]*b[1],a[0]*b[1]+a[1]*b[0]+a[1]*b[1]]

def nf(n):
    if n == 0: return 1
    a, F = [0,1], [[0,1]]
    while F[-1][0] < n:
        a = fibmult(a,a)
        F.append(a)
    k, f = 2, F[-2]
    while k < len(F) and f[1] < n:
        k += 1
        while k < len(F) and fibmult(f,F[-k])[0] > n: k += 1
        f = fibmult(f,F[-k])
    if n-f[0] <= f[1]-n: return f[0]
    return f[1]
