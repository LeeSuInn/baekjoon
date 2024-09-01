engword = input()
countlist = [0] * 100

for i in engword:
  n = ord(i)
  if n > 96:
    n = n - 32
  countlist[n] += 1

maxresult = max(countlist)
if countlist.count(maxresult) > 1:
  print("?")
else:
  print(chr(countlist.index(maxresult)))