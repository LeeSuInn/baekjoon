n = int(input())

value = list(map(int, input().split()))

print(max(value) * min(value))