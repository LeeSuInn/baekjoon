n = int(input())
value = list(map(int, input().split(" ")))

for i in range(1, n):
    value[i] = max(value[i], value[i] + value[i - 1])

print(max(value))