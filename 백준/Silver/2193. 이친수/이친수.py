n = int(input())
result = [[0] * 2 for _ in range(91)]

result[1] = [0, 1]

for i in range(2, 91):
    result[i][0] = result[i-1][0] + result[i-1][1]
    result[i][1] = result[i-1][0]

print(sum(result[n]))