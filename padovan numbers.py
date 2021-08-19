from math import log2

def padmult(a,b):
    return [a[0]*b[0]+a[1]*b[2]+a[2]*b[1],
           a[1]*b[1]+a[2]*b[2]+a[0]*b[1]+a[1]*b[0],
           a[1]*b[1]+a[0]*b[2]+a[2]*b[0]+a[1]*b[2]+a[2]*b[1]]

def padovan(n):
    power=(n+5)//3
    bipos=[]
    while power!=0:
        bipos.append(int(log2(power)))
        power=power%(2**bipos[-1])
    bipos.reverse()
    a=[1,0,1]
    for k in range(bipos[0]): a=padmult(a,a)
    p=a
    for i in range(1,len(bipos)):
        for k in range(bipos[i]-bipos[i-1]): a=padmult(a,a)
        p=padmult(a,p)
    return p[(n+2)%3]
