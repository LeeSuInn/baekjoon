n = int(input())
s = input().split()
stack = []
result = ["-1" for i in range(n)]
count_dict = {}

for i in range(n):
    if s[i] in count_dict:
        count_dict[s[i]] += 1
    else:
        count_dict[s[i]] = 1

for i in range(n):
    while stack and count_dict[s[i]] > count_dict[s[stack[-1]]]:
        result[stack.pop()] = s[i]
    stack.append(i)

print(" ".join(result))