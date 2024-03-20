import sys

que = []

n = int(sys.stdin.readline())

for i in range(n):
    order = sys.stdin.readline().split()

    if order[0] == "push":
        que.append(order[1])
    
    elif order[0] == "pop":
        if not que:
            print(-1)
            continue
        print(que.pop(0))
    
    elif order[0] == "size":
        print(len(que))

    elif order[0] == "empty":
        if not que:
            print(1)
        else:
            print(0)
    
    elif order[0] == "front":
        if not que:
            print(-1)
            continue
        print(que[0])
    
    else:
        if not que:
            print(-1)
            continue
        print(que[-1])