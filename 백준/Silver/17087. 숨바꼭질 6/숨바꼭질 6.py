import math

n, s = map(int, input().split(" "))

location = list(map(int, input().split(" ")))

for i in range(n):
    location[i] -= s

abs_locations = [abs(x) for x in location]
result = math.gcd(*abs_locations)

print(result)