from math import log2, log10
from datetime import datetime

def padmult(a,b):
    return [a[0]*b[0]+a[1]*b[2]+a[2]*b[1],
           a[1]*b[1]+a[2]*b[2]+a[0]*b[1]+a[1]*b[0],
           a[1]*b[1]+a[0]*b[2]+a[2]*b[0]+a[1]*b[2]+a[2]*b[1]]

# preferable:

def padovan2(n):
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
         
# since log2 seems to be forbidden:

def binpow(n):
    res=[]
    while n>0:
        k=0
        while 2**k<=n: k+=1
        res.append(k-1)
        n=n%(2**(k-1))
    res.reverse()
    return res
    
def padovan2(n):
    bipos=binpow((n+5)//3)
    print(bipos)
    a=[1,0,1]
    for k in range(bipos[0]): a=padmult(a,a)
    p=a
    for i in range(1,len(bipos)):
        for k in range(bipos[i]-bipos[i-1]): a=padmult(a,a)
        p=padmult(a,p)
    return p[(n+2)%3]

# or, using bin function:

def padovan2(n):
    bipozeros=bin((n+5)//3)[2:].split('1')
    bipodiffs=[len(word)+1 for word in bipozeros[1:-1]]+[len(bipozeros[-1])]
    bipodiffs.reverse()
    a=[1,0,1]
    for k in range(bipodiffs[0]): a=padmult(a,a)
    p=a
    for bipodiff in bipodiffs[1:]:
        for k in range(bipodiff): a=padmult(a,a)
        p=padmult(a,p)
    return p[(n+2)%3]



    

n=9

starttime=datetime.now()
print(padovan2(n))
print(format(datetime.now()-starttime))

#starttime=datetime.now()
#print(padovan1(n))
#print(format(datetime.now()-starttime))

