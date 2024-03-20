n, b = map(int, input().split(" "))

result = ""

while n != 0:
    rest = n % b
    n //= b

    if b > 10:
        if rest < 10:
            result = str(rest) + result
        else:
            result = chr(55 + rest) + result
    else:
        result = str(rest) + result

print(result)