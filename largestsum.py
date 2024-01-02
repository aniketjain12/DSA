def larg_cont_sum(arr):
  if len(arr)==0:
    return 0

  max_sum = current_max = arr[0]
  for num in arr[1:]:
    current_max = max(current_max+num,num)
    max_sum = max(current_max,max_sum)

  return max_sum

a=larg_cont_sum([1,2,-1,3,4,10,10,-10,-1])
print(a)