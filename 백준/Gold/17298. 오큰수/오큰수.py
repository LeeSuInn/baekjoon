n = int(input())
s = input().split()
result = ["-1" for _ in range(n)]
stack = []

for i in range(n):
    while stack and int(s[i]) > int(s[stack[-1]]):
        result[stack.pop()] = s[i]
    stack.append(i)

print(" ".join(result))