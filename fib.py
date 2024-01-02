'''
def fib_rec(n):
  if n == 0 or n == 1:
    return n

  else:
    return fib_rec(n-1)+fib_rec(n-2)

f = fib_rec(10)
print(f)

def fib_iter(n):
  a,b=0,1
  for i in range(n):
    a,b = b,a+b

  return a

f1 = fib_iter(10)
print(f1)
'''
n = 10
cache = [None]*(n+1)
def fib_dyn(n):
  if n ==0 or n==1:
    return n

  if cache[n] != None:
    return cache[n]

  cache[n] = fib_dyn(n-1)+fib_dyn(n-2)
  return cache[n]

f2 = fib_dyn(10)
print(f2)
  