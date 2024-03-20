import sys

n = int(sys.stdin.readline())
result = [0] * 10001

for i in range(n):
    result[int(sys.stdin.readline())] += 1

for i in range(len(result)):
    if result[i] != 0:
        for j  in range(result[i]):
            print(i)