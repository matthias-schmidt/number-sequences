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
