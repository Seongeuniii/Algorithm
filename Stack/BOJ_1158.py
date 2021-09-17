import sys
from collections import deque
n, k = map(int,sys.stdin.readline().split())
stack = deque([i for i in range(n,0,-1)])
result = []
while len(stack) != 0:
    for _ in range(k-1):
        a = stack.pop()
        stack.appendleft(a)
    a = stack.pop()
    result.append(str(a))
print("<",", ".join(result)[:],">", sep='')