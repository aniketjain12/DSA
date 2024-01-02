def bubble_sort(arr):
  for n in range(len(arr)-1,0,-1):
    print('The value of n: ',n)
    for k in range(n):
      print('The k is: ',k)
      if arr[k]>arr[k+1]:
        temp = arr[k]
        arr[k] = arr[k+1]
        arr[k+1] = temp

  return arr

arr = [5,3,7,2]
a = bubble_sort(arr)
print(a)