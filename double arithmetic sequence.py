def dlsequence(n):
    u=[1]
    xi,yi = 0,0
    x,y = 3,4
    for i in range(n):
        if x<y:
            u.append(x)
            xi+=1
            x=2*u[xi]+1
        else:
            u.append(y)
            if x==y:
                xi+=1
                x=2*u[xi]+1
            yi+=1
            y=3*u[yi]+1
    return u[-1]
