'''
def finder(arr1,arr2):
  arr1.sort()
  arr2.sort()
  for num1,num2 in zip(arr1,arr2):
    if num1 != num2:
      return num1

  return arr1[-1]

s = finder([5,5,3],[5,5])
print(s)
'''

import collections
def finder2(arr1,arr2):
  d=collections.defaultdict(int)
  for num in arr2:
    d[num]+=1

  for num in arr1:
    if d[num]==0:
      return num

    else:
      d[num]-=1

s = finder2([5,5,3],[5,5])
print(s)
'''
def finder3(arr1,arr2):
  result = 0
  for num in arr1+arr2:
    result ^= num
    print(result)
    
  print('\n')
  return result

s= finder3([5,5,7],[5,5])
print(s)
'''