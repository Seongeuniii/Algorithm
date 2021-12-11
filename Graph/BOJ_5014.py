import sys
from collections import deque
F, S, G, U, D = map(int,input().split()) #총, 강호, 스탙,
visited = [0]*(F+1)

def bfs(start):
  q = deque()
  if start == G:
    return 0
  q.append((start,0))
  visited[start] = 1
  while q:
    s,cnt = q.popleft()
    us = s+U
    ds = s-D
    if us <= F and not visited[us]:
      visited[us] = 1
      q.append((us,cnt+1))
    if ds > 0  and not visited[ds]:
      visited[ds] = 1 
      q.append((ds,cnt+1))
    if us == G or ds == G:
      return cnt+1
  return -1

answer = bfs(S)
if answer == -1: print('use the stairs')
else: print(answer)
  