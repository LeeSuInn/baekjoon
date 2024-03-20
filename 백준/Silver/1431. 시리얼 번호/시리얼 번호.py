def sum(num):
    result = 0
    for c in num:
        if c.isdigit():
            result += int(c)
    return result

n = int(input())
result = []
for i in range(n):
    result.append(input())

result.sort(key = lambda x: (len(x), sum(x), x))

for c in result:
    print(c)
