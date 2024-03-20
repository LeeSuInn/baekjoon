s = input()
check = 0
cnt = 0
result = 0

for i in s:
    if i == "(":
        cnt += 1
        check = 1

    else:
        if cnt == 1 and check == 1:
            cnt -= 1
            check = 0
        elif cnt != 1 and check == 1:
            cnt -= 1
            result += cnt
            check = 0
        elif cnt != 1 and check == 0:
            result += 1
            cnt -= 1
        elif cnt == 1 and check == 0:
            result += 1
            cnt -= 1

print(result)