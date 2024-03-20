n = int(input())
stack = []
result = []
output = []

current = 1  # 스택에 넣을 다음 숫자를 나타내는 변수

for i in range(n):
    num = int(input())

    while current <= num:
        stack.append(current)
        output.append("+")
        current += 1

    if stack[-1] == num:
        stack.pop()
        output.append("-")
    else:
        print("NO")
        exit(0)

for op in output:
    print(op)