import sys
from collections import deque
input = sys.stdin.readline

def solution():
  if order[0] != 1:
    return 0

  q = deque([order[0]])
  check[order[0]] = 1
  idx = 1

  while q:
    dq = q
    q = deque()

    while dq:
      cnt = 0
      node = dq.popleft()

      for nd in graph[node]:
        if not check[nd]:
          check[nd] = 1
          cnt += 1

      for i in range(idx, idx + cnt):
        if not check[order[i]]:
          return 0
        q.append(order[i])

      idx += cnt

  return 1

N = int(input())
graph = [[] for _ in range(N+1)]
check = [0 for _ in range(N+1)]

for _ in range(N-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

order = list(map(int, input().split()))

print(solution())