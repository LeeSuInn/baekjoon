n = int(input())
value = list(map(int, input().split(" ")))
dp = [1] * n
result = []
for i in range(1, n):
    for j in range(i):
        if value[i] > value[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

order = max(dp)
for i in range(n - 1, -1, - 1 ):
    if order == dp[i]:
        result.append(value[i])
        order -= 1
result.reverse()
print(*result)