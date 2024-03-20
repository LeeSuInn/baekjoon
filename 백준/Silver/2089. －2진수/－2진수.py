n = int(input())
result = ""
if not n:
    print("0")
    exit()
while n:
    if n % -2:
        result = "1" + result
        n = n // -2 + 1
    else:
        result = "0" + result
        n = n // -2

print(result)