def permute(s):
  out = []
  if len(s) == 1:
    out = [s]

  else:
    for i,let in enumerate(s):
      for perm in permute(s[:i]+s[i+1:]):
        print('The length is',let)
        print('The Perm is:',perm)
        out +=[let+perm]

  return out

p = permute('abc')
print(p)