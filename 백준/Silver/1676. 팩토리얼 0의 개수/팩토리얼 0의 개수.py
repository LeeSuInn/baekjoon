n = int(input())
result = 1
count = 0
for i in range(1, n + 1):
    result *= i

Result = reversed(str(result))

for c in Result:
    if c == '0':
        count += 1
    else:
        print(count)
        break

