n, b = input().split(" ")

result = 0
length = len(n) - 1

for i in n:
    if int(b) > 10:
        if ord(i) < 58:
            result += (ord(i)- 48) * (int(b) ** length)
        else:
            result += (ord(i) - 55) * (int(b) ** length)
    else:
        result += int(i) * (int(b) ** length)
    length -= 1

print(result)