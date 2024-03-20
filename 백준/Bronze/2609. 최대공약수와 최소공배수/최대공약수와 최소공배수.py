num = input().split(" ")

num1 = int(num[0])
num2 = int(num[1])

for i in range(1, num1 + 1):
    if num1 % i == 0 and num2 % i == 0:
        max = i

for i in range(1, num2 + 1):
    if (i * num1) % num2 == 0:
        min = i * num1
        break
    
print(max)
print(min)