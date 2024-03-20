n =  int(input())
postfix = list(input())
stack = []
value = []
for i in range(n):
    value.append(int(input()))

for c in postfix:
    if c.isalpha():
        for j in range(n):
            if c == chr(65 + j):
                c = value[j]
                break
        stack.append(c)
    else:
        피연산자1 = stack.pop()
        피연산자2 = stack.pop()
        if c == '+':
            stack.append(피연산자2 + 피연산자1)
        elif c == '-':
            stack.append(피연산자2 - 피연산자1)
        elif c == '*':
            stack.append(피연산자2 * 피연산자1)
        else:
            stack.append(피연산자2 / 피연산자1)

result = stack[0]
print("{:.2f}".format(result))
