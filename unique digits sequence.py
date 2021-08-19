def uds(n):
    f, ld, ldre, gaps, fmax = 0, '123456789', re.compile(', [1-9]*, '), ', ', 0
    alldigits, maxrange = {'0','1','2','3','4','5','6','7','8','9'}, 10*n
    for k in range(1,n+1):
        m = ldre.search(gaps)
        if m:
            ms = m.span()
            fs = gaps[ms[0]+2:ms[1]-2]
            f = int(fs)
            ld = ''.join(sorted(alldigits-set(fs)))
            ldre = re.compile(', ['+ld+']*, ')
            gaps = gaps[:ms[0]+2]+gaps[ms[1]:]
        else:
            fs = str(fmax + 1)
            while any(d not in ld for d in fs):
                for j in range(len(fs)):
                    if fs[j] not in ld:
                        fs = str(int(fs[:j+1]) + 1) + ld[0] * (len(fs)-j-1)
                        break
            f = int(fs)
            ld = ''.join(sorted(alldigits-set(fs)))
            ldre = re.compile(', ['+ld+']*, ')
            if f > fmax+1: gaps += ', '.join([str(i) for i in range(fmax+1,f)]) + ', '
            fmax = f
    return f




# with cache (performance version)

cache = {0:0, -1:0, -2:0, -3:', '}

def udsc(n):
    if n < cache[-1]: return cache[n]
    kstart, fmax, gaps = cache[-1], cache[-2], cache[-3]
    alldigits, maxrange = {'0','1','2','3','4','5','6','7','8','9'}, 10*n
    ld = ''.join(sorted(alldigits-set(str(cache[cache[-1]]))))
    ldre = re.compile(', ['+ld+']*, ')
    for k in range(kstart+1,n+1):
        m = ldre.search(gaps)
        if m:
            ms = m.span()
            fs = gaps[ms[0]+2:ms[1]-2]
            f = int(fs)
            ld = ''.join(sorted(alldigits-set(fs)))
            ldre = re.compile(', ['+ld+']*, ')
            gaps = gaps[:ms[0]+2]+gaps[ms[1]:]
        else:
            fs = str(fmax + 1)
            while any(d not in ld for d in fs):
                for j in range(len(fs)):
                    if fs[j] not in ld:
                        fs = str(int(fs[:j+1]) + 1) + ld[0] * (len(fs)-j-1)
                        break
            f = int(fs)
            ld = ''.join(sorted(alldigits-set(fs)))
            ldre = re.compile(', ['+ld+']*, ')
            if f > fmax+1: gaps += ', '.join([str(i) for i in range(fmax+1,f)]) + ', '
            fmax = f
        cache.update({k:f})
    cache[-1] = n
    cache[-2] = fmax
    cache[-3] = gaps
    return f
