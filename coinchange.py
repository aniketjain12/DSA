def rec_coin(target,coin):
  min_coin = target
  if target in coin:
    return 1

  else:
    for i in[c for c in coin if c<=target]:
      num_coin = 1+ rec_coin(target-i,coin)
      if num_coin <min_coin:
        min_coin = num_coin

    return min_coin

r = rec_coin(10,[1,5])
print(r)