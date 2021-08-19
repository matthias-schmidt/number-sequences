from math import log2, log10
from datetime import datetime

def uds(n):
    f, gaps, used = 0, [], set()
    for k in range(1,n+1):
        i = 0
        lastdigits = set(str(f))
        try:
            f = [g for g in gaps if len(lastdigits & set(g)) == 0][0]
            gaps.remove(f)
            f = int(f)
        except:
            i = k
            while i in used or lastdigits & set(str(i)): i += 1
            f = i
            used.add(f)
        if k not in used: gaps.append(str(k))
        else: used.remove(k)
    return f, min(gaps), len(used)



def uds2(n):
    f, lastdigits, gaps, used = 0, {0}, [], set()
    for k in range(1,n+1):
        i = 0
        while i < len(gaps) and lastdigits & set(gaps[i]): i += 1
        if i < len(gaps):
            f = int(gaps[i])
            lastdigits = set(gaps[i])
            gaps.remove(gaps[i])#gaps = gaps[:i]+gaps[i+1:]
        else:
            i = k
            while i in used or lastdigits & set(str(i)): i += 1
            f = i
            lastdigits = set(str(f))
            used.add(f)
        if k not in used: gaps.append(str(k))
        else: used.remove(k)
    return f, gaps, used






def uds3(n):
    f, fmax, gaps = 0, 0, []
    for k in range(1,n+1):
        i = 0
        lastdigits = set(str(f))
        while i < len(gaps) and len(lastdigits & set(str(gaps[i]))): i += 1
        if i < len(gaps):
            f = gaps[i]
            gaps.remove(f)
        else:
            i = fmax + 1
            while len(lastdigits & set(str(i))): i += 1
            f = i
            gaps.extend(range(fmax+1,f))
            fmax = f
    return f, gaps


# using a counter running through admissible digits only (slower for some reason):

def uds2(n):
    f, lastdigits, gaps, used = 0, {0}, [], set()
    maxrange = 10*n
    jump, count = 0, 0
    for k in range(1,n+1):
        chk = 0
        for i in range(len(gaps)):
            if not lastdigits.intersection(gaps[i]):
                f = gaps[i]
                lastdigits = set(gaps[i])
                gaps.remove(gaps[i])
                chk = 1
                #print(k,'from gap',f)
                #input()
                break
        if chk == 0:
            #digits = [char for char in ["0","1","2","3","4","5","6","7","8","9"] if char not in lastdigits]
            digits = sorted({"0","1","2","3","4","5","6","7","8","9"} - lastdigits)
            start = tuple(str(k))
            #print(lastdigits,digits)
            try:
                ctrran = list(product(digits, repeat = len(start)))
                startctr = bisect_left(ctrran,start)
                ctr = (i for i in ctrran[startctr:])
                while True:
                    f = ''.join(next(ctr))
                    #print('check whether in used a',f)
                    if f not in used:
                        lastdigits = set(f)
                        used.add(f)
                        break
            except:
                startctr = 0
                ctrran = list(product(digits, repeat = len(start)+1))
                if '0' in digits:
                    startctr = bisect_left(ctrran,tuple(digits[1]) + tuple('0') * len(start))
                ctr = (i for i in ctrran[startctr:])
                while True:
                    f = ''.join(next(ctr))
                    #print('check whether in used b',f)
                    if f not in used:
                        lastdigits = set(f)
                        used.add(f)
                        break
            #print(k,'from used',f)
            #input()
        if str(k) not in used: gaps.append(str(k))
        else: used.remove(str(k))
    return f, len(gaps), len(used)#, jump, count



from itertools import product
from bisect import bisect_left


def count(start,ex):
    digits = [char for char in ["0","1","2","3","4","5","6","7","8","9"] if char not in ex]
    start = tuple(str(start))
    length = len(start)
    startctr = bisect_left(list(product(digits, repeat = length)),start)
    ctr = (i for i in list(product(digits, repeat = length))[startctr:])
    res = []
    for i in range(3):
        res.append(''.join(next(ctr)))
    return res



def uds1(n):
    f, lastdigits, gaps, used = 0, {0}, [], set()
    maxrange = 10*n
    for k in range(1,n+1):
        chk = 0
        for i in range(len(gaps)):
            if not lastdigits.intersection(gaps[i]):
                f = int(gaps[i])
                lastdigits = set(gaps[i])
                gaps.remove(gaps[i])
                chk = 1
                break
        if chk == 0:
            start = str(k)
            for digit in "0123456789":
                if digit not in lastdigits:
                    minfree = digit
                    break
            while lastdigits.intersection(start):
                for j in range(len(start)):
                    if start[j] in lastdigits:
                        start = str(int(start[:j+1]) + 1) + minfree * (len(start)-j-1)
                        break
            for i in range(int(start),maxrange):
                if i not in used:
                    if not lastdigits.intersection(str(i)):
                        f = i
                        lastdigits = set(str(i))
                        used.add(i)
                        break
        if k not in used: gaps.append(str(k))
        else: used.remove(k)
    return f, len(gaps), len(used)



# same with regex for lastdigits:

import re

def uds(n):
    f, ld, ldre, gaps, used, = 0, '123456789', re.compile(', [1-9]*, '), ', ', set()
    alldigits, maxrange = {'0','1','2','3','4','5','6','7','8','9'}, 10*n
    for k in range(1,n+1):
        #print(k)
        m = ldre.search(gaps)
        if m:
            ms = m.span()
            fs = gaps[ms[0]+2:ms[1]-2]
            f = int(fs)
            ld = ''.join(sorted(alldigits-set(fs)))
            ldre = re.compile(', ['+ld+']*, ')
            gaps = gaps[:ms[0]+2]+gaps[ms[1]:]
            #gaps = gaps.replace(fs+', ', '')
        else:
            start = str(k)
            while any(d not in ld for d in start):
                for j in range(len(start)):
                    if start[j] not in ld:
                        start = str(int(start[:j+1]) + 1) + ld[0] * (len(start)-j-1)
                        break
            #print('start',start)
            for i in range(int(start),maxrange):
                if i not in used:
                    if all(d in ld for d in str(i)):
                        f = i
                        ld = ''.join(sorted(alldigits-set(str(f))))
                        #print('used branch')
                        ldre = re.compile(', ['+ld+']*, ')
                        used.add(i)
                        break
        if k not in used: gaps += str(k) + ', '
        else: used.remove(k)
        #print('f',f)
        #print('ld',ld)
        #print('gaps',gaps)
        #print('used',used)
        #input()
    return f, len(gaps), len(used)


########################################################################################


# with recording only the gaps (fastest)

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




# with cache, works also on CW and passes tests in time

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



# soln from CW, less time grow (twice as fast for 40000):

from collections import deque
from itertools import product

class Seq(object):
    def __init__(self):
        self.bit_cache = []
        self.seq_cache = []
        self.used = [False] * 1000000
        self.queue = [deque() for _ in range(1024)]
        self.upper_bound = 10
        self.last_pat = 0
        self.gen_queue(True)
            
    def bit(self, n):
        if len(self.bit_cache) > n:
            return self.bit_cache[n]
        for i in range(len(self.bit_cache), n+1):
            bits = 0
            while i:
                bits |= 2 ** (i % 10)
                i //= 10
            self.bit_cache.append(bits)
        return self.bit_cache[n]
    def gen_queue(self, init=False):
        range_ = range(self.upper_bound)
        if not init:
            range_ = range(self.upper_bound, self.upper_bound * 2)
            self.upper_bound *= 2
        for i in range_:
            bit = self.bit(i)
            comb = [(0, b) for b in (1, 2, 4, 8, 16, 32, 64, 128, 256, 512) if (b & bit) == 0]
            for p in product(*comb):
                self.queue[sum(p)].append(i)
    def seq(self, n):
        if len(self.seq_cache) > n:
            return self.seq_cache[n]
        for i in range(len(self.seq_cache), n+1):
            next_seq = 0
            while True:
                while len(self.queue[self.last_pat]) == 0:
                    self.gen_queue()
                next_seq = self.queue[self.last_pat].popleft()
                if not self.used[next_seq]:
                    self.used[next_seq] = True
                    break
            self.seq_cache.append(next_seq)
            self.last_pat = self.bit(next_seq)
        return self.seq_cache[n]


seq = Seq()

def find_num(n):
    return seq.seq(n)







#digits = "1357"
#start = ('3', '7')
#startctr = bisect_left(list(product(digits, repeat = 2)),start)

#print(startctr)
#input()
#countr = (i for i in list(product(digits, repeat = 2))[startctr:])

#while True:
#    a = next(countr)
#    print(a[0]+a[1])
#    input()


#print(count(41,{'2','4'}))

n = 40000

starttime=datetime.now()
print(uds(n))
print(format(datetime.now()-starttime))

starttime=datetime.now()
print(find_num(n))
print(format(datetime.now()-starttime))
input()




for n in [10000,20000,30000,40000,50000,60000]:
    print(cache[-1])
    starttime=datetime.now()
    print(udsc(n))
    print(format(datetime.now()-starttime))

#starttime=datetime.now()
#print(uds1(n))
#print(format(datetime.now()-starttime))


