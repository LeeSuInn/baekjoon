n = int(input())

result = [0] * 11
result[1] = 1
result[2] = 2
result[3] = 4

for i in range(n):
    key = int(input())
    for j in range(4, key + 1):
        if result[j] == 0:
            result[j] = result[j - 1] + result[j-2] + result[j-3]
    print(result[key])