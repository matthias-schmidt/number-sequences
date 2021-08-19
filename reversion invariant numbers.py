def reverse2(n):
    factor=len(str((n+1)//2))-1
    if n<=11*10**factor-1:
        seed=str(n-10**factor)
        return int(seed+seed[0:factor][::-1])
    else:
        seed=str(n-10**(factor+1))
        return int(seed+seed[::-1])
