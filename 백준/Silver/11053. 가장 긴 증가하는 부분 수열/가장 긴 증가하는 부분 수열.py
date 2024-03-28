n = int(input())

result = list(map(int, input().split(" ")))
dp = [1] * n
check = True
for i in range(1, n):
    for j in range(i):
        if result[i] > result[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))