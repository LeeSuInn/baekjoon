num = input().split(" ")
for i in range(int(num[0]), int(num[1]) + 1):
    check = False
    for n in range(2, int(i**(0.5)) + 1):
        if i % n == 0:
            check = True
            break
    if not check and i != 1:
        print(i)