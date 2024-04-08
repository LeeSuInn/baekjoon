T = int(input())
result = [0] * 1000001
result[1] = 1
result[2] = 2
result[3] = 4
for i in range(4, 1000001):
    result[i] = (result[i-1] + result[i-2] + result[i-3]) % 1000000009

for i in range(T):
    n = int(input())
    print(result[n])