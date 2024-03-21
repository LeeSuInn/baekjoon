n = int(input())
result = 2
while n != 1:
    if n % result == 0:
        print(result)
        n //= result
    else:
        result += 1