'''
def seq_search(arr,ele):
  pos = 0
  found = False
  while pos < len(arr) and not found:
    if arr[pos] == ele:
      found = True

    else:
      pos +=1

  return found
'''
def order_seq_search(arr,ele):
  pos = 0
  found = False
  stopped = False

  while pos < len(arr) and not found and not stopped:
    if arr[pos] == ele:
      found = True

    else:
      if arr[pos] > ele:
        stopped = True

      else:
        pos += 1

  return found
 
arr1 =[1,2,3,4,5]
a = order_seq_search(arr1,1)
print(a)