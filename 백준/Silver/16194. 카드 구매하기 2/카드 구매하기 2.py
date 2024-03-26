n = int(input())

value = list(map(int, input().split(" ")))
result = value
value.insert(0, 0)

for i in range(1, n + 1):
    for j in range(1, i + 1):
        result[i] = min(result[i], result[i - j] + value[j])
print(result[n])