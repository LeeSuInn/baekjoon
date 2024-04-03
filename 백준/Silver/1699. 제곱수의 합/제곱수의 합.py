n = int(input())

result = [x for x in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if i < j*j:
            break
        if result[i] > result[i - j*j] + 1:
            result[i] = result[i - j*j] + 1

print(result[n])