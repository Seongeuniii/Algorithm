import sys
from collections import deque
N,K = map(int,input().split())
if K <= N:
  print(N-K)
  sys.exit()
visited = [0]*(2*K+1)
q = deque()
q.append((N,0))
visited[N] = 1 
def check(nd,c):
  if nd > 2*K or nd < 0:
    return
  if nd == K:
    print(c+1)
    sys.exit()
  if not visited[nd]:
    visited[nd] = 1
    q.append((nd,c+1))
while q:
  node, cnt = q.popleft()
  check(node+1,cnt)
  check(node-1,cnt)
  check(node*2,cnt)