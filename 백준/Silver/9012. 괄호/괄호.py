n = int(input())

for i in range(n):
    s = list(input())
    stack = []

    for bracket in s:
        if bracket == '(':
            stack.append('(')
        elif bracket == ')':
            if not stack:
                stack.append(')')
                break
            stack.pop()
    if not stack:
        print("YES")
    else:
        print("NO")