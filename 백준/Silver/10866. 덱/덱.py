from collections import deque
import sys

Deque = deque()
n = int(sys.stdin.readline())

for i in range(n):
    order = list(sys.stdin.readline().split())

    if order[0] ==  "push_front":
        Deque.appendleft(order[1])

    elif order[0] ==  "push_back":
        Deque.append(order[1])
    
    elif order[0] ==  "pop_front":
        if not Deque:
            print(-1)
            continue
        print(Deque.popleft())

    elif order[0] ==  "pop_back":
        if not Deque:
            print(-1)
            continue
        print(Deque.pop())

    elif order[0] ==  "size":
        print(len(Deque))

    elif order[0] ==  "empty":
        if not Deque:
            print(1)
        else:
            print(0)

    elif order[0] ==  "front":
        if not Deque:
            print(-1)
            continue
        print(Deque[0])

    else:    
        if not Deque:
            print(-1)
            continue
        print(Deque[len(Deque) - 1])