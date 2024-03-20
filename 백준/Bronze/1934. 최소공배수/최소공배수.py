import math
n = int(input())

for i in range(n):
    num = input().split(" ")
    num1 = int(num[0])
    num2 = int(num[1])
    
    print(math.lcm(num1, num2))