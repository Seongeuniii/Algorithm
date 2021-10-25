from collections import deque
N, K = map(int,input().split())
q = deque([i for i in range(N,0,-1)])
result = []
while q:
  for i in range(K-1):
    q.appendleft(q.pop())
  result.append(str(q.pop()))
print('<',', '.join(result),'>',sep='')