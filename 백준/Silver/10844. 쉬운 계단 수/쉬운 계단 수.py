n = int(input())

result = [[0] * 10 for _ in range(101)]
result[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, 101):
    for j in range(0, 10):
        if j == 0:
            result[i][j] = result[i-1][j+ 1] % 1000000000
        elif j ==9:
            result[i][j] = result[i-1][j-1] % 1000000000
        else:
            result[i][j] = (result[i-1][j-1] + result[i-1][j +1]) % 1000000000

print(sum(result[n]) % 1000000000)