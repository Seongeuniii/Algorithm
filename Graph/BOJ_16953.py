import sys
from collections import deque

A,B  = map(int,input().split())

q = deque()
q.append((A,1))

while q:
  a, cnt = q.popleft()
  t1 = a*2
  t2 = int(str(a)+'1')

  if t1 == B or t2 == B:
      print(cnt+1)
      sys.exit()

  if t1 <= B:
    q.append((t1, cnt+1))
  if t2 <= B:
    q.append((t2, cnt+1))

print(-1)