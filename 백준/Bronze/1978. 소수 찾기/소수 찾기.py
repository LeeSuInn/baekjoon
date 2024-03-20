n = int(input())
result = n
numbers = (input().split(" "))

for i in numbers:
    num = int(i)

    if num == 1:
        result -= 1
    else:
        for j in range(2, num):
            if num % j == 0:
                result -= 1
                break

print(result)