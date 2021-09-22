import sys
from collections import deque
n = int(sys.stdin.readline())
queue = deque()
for _ in range(n):
    a = sys.stdin.readline().strip().split()
    if a[0] == 'push':
        queue.append(int(a[1]))
    elif a[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif a[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    elif a[0] == 'size':
        print(len(queue))
    else:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())