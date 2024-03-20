alphastr = input()
result = [-1] * 26

for c in alphastr:
    result[ord(c)- 97] = alphastr.index(c)

Result = " ".join(map(str,result))
print(Result)