def fibmult(a,b):
    return [a[0]*b[0]+a[1]*b[1],a[0]*b[1]+a[1]*b[0]+a[1]*b[1]]

def fibonacci(arg):
    n = abs(arg)
    if arg < 0: s = (-1)**(n%2+1)
    else: s = 1
    brg = bin(n+1)[3:].split('1')[::-1]                     # bin rep gaps
    br = [len(brg[0])]+[len(gap)+1 for gap in brg[1:]]      # bin rep n+1 = 2**b[0] + 2**(b[0]+b[1]) + ...
    a, f = [0,1], [1,0]                                     # fib seq seeds
    for i in range(len(br)):
        for k in range(br[i]): a = fibmult(a,a)
        f = fibmult(a,f)
    return s * f[0]



# by calling a single function. a bit faster

def fib(n):
  if n < 0: return (-1)**(n % 2 + 1) * fib(-n)
  a = b = x = 1
  c = y = 0
  while n:
    if n % 2 == 0:
      (a, b, c) = (a * a + b * b,
                   a * b + b * c,
                   b * b + c * c)
      n /= 2
    else:
      (x, y) = (a * x + b * y,
                b * x + c * y)
      n -= 1
  return y
