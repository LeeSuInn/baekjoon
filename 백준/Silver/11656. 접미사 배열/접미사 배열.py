Str = input()
result = []

for i in range(len(Str)):
    result.append(Str[i:])

for c in sorted(result):
    print(c)