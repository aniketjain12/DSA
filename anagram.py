'''
def anagram(s1,s2):
  s1 = s1.replace(' ','').lower()
  s2 = s2.replace(' ','').lower()
  return sorted(s1) == sorted(s2)

anagram('blam','lamb')
'''

def anagram(s1,s2):
  s1 = s1.replace(' ','').lower()
  s2 = s2.replace(' ','').lower()
  
  if len(s1) != len(s2):
    print('No')
    break
  count = {}
  for letter in s1:
    if letter in count:
      count[letter]+=1

    else:
      count[letter]=1

  for letter in s2:
    if letter in count:
      count[letter]-=1

    else:
      count[letter]=1

  for k in count:
    if count[k] != 0:
      print('No')
      break

  print('Yes')

anagram('lamb','blam')


