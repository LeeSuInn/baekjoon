n = int(input())

result = [([0] * 3) for _ in range(100001)]
result[1] = [1, 0, 0]
result[2] = [0, 1, 0]
result[3] = [1, 1, 1]

for i in range(4, 100001):
    result[i][0] = result[i-1][1] + result[i-1][2] % 1000000009
    result[i][1] = result[i-2][0] + result[i-2][2] % 1000000009
    result[i][2] = result[i-3][0] + result[i-3][1] % 1000000009


for i in range(n):
    T = int(input())
    print(sum(result[T])%1000000009)