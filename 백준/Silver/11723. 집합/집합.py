import sys
n = int(input())
emptygrp = set()

for i in range(n):
  result = sys.stdin.readline().split()
  action = result[0]
  
  if len(result) == 1:
    if action == 'all':
      emptygrp = set(range(1, 21))
    else:
      emptygrp.clear()
    continue
  
  num = int(result[1])

  if action == 'add':
    emptygrp.add(num)
  elif action == 'remove':
    emptygrp.discard(num)
  elif action == 'toggle':
    if num in emptygrp:
      emptygrp.discard(num)
    else:
      emptygrp.add(num)
  else:
    print(1 if num in emptygrp else 0)



