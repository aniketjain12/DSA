def selection_sort(arr):
  for fillslot in range(len(arr)-1,0,-1):
    print('The value of fillslot: ',fillslot)
    positionOfMax = 0
    for location in range(1,fillslot+1):
      print('The location: ',location)
      if arr[location] > arr[positionOfMax]:
        positionOfMax = location
        print('The pom is: ',positionOfMax)

    temp = arr[fillslot]
    arr[fillslot] = arr[positionOfMax]
    arr[positionOfMax] = temp
  return arr

arr = [5,8,3,10,1]
a = selection_sort(arr)
print(a)