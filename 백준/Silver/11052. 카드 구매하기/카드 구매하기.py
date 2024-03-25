n = int(input())

value = list(map(int, input().split(" ")))
value.insert(0, 0)
result = [0] * (n + 1)

for i in range(1, n+ 1):
    for j in range(1, i + 1):
        result[i] = max(result[i], result[i - j] + value[j])

print(result[n])