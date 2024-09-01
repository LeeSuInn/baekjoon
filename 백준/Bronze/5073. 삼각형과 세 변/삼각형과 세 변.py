while True:
  lengthlist = list(map(int,input().split(" ")))
  lengthlist.sort()

  if lengthlist[0] == 0 and lengthlist[1] == 0 and lengthlist[2] == 0:
    break
  elif lengthlist[2] >= lengthlist[0] + lengthlist[1]:
    print("Invalid")
  elif lengthlist[0] == lengthlist[2]:
    print("Equilateral")
  elif (lengthlist[0] == lengthlist[1]) | (lengthlist[1] == lengthlist[2]):
    print("Isosceles")
  else:
    print("Scalene")