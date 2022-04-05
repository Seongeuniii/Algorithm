from collections import deque

N = int(input())
q = deque([i for i in range(1, N+1)])

while len(q) >= 2:
  print(q.popleft(), end = ' ')
  q.append(q.popleft())

print(q[0])