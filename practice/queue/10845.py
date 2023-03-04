import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque()

for _ in range(n):
    command = list(sys.stdin.readline().split())

    if command[0] == 'push':
        q.append(command[1])
    elif command[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
    else:
        if q:
            print(0)
        else:
            print(1)

