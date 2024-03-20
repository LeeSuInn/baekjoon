import sys
n = int(sys.stdin.readline())
stack = []

for i in range(n):
    strlist = sys.stdin.readline().split()
    
    if(strlist[0] == "push"):
        stack.append(strlist[1])
    elif(strlist[0] == "pop"):
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif(strlist[0] == "size"):
        print(len(stack))
    elif(strlist[0] == "empty"):
        if(len(stack) == 0):
            print(1)
        else:
            print(0)
    elif(strlist[0] == "top"):
        if not stack:
            print(-1)
        else:
            print(stack[len(stack)-1])
