'''
def fact(n):
  if n == 0:
    return 1

  else:
    return n * fact(n-1)

f=fact(4)
print(f)

def re_sum(n):
  if n == 0:
    return 0

  else:
    return n + re_sum(n-1)

r = re_sum(4)
print(r)

def sum_func(n):
  if len(str(n)) == 1:
    return n

  else:
    return n%10 + sum_func(n/10)

s = sum_func(4321)
print(s)
'''
