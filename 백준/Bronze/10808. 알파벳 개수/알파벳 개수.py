alphastr = input()
result = [0] * 26

for c in alphastr:
    result[ord(c)- 97] += 1

result.reverse()
while result:
    print(result.pop(),end = " ")