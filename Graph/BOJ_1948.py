import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
indeg = [0 for _ in range(N+1)]

for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    indeg[b] += 1

start,end = map(int,input().split())

time = [0]*(N+1) # 시간
parent = [[] for _ in range(N+1)]

q = deque()
q.append(start)

while q:
    node = q.popleft() 
    if node == end:
        continue
    for nd,tm in graph[node]:
        indeg[nd]-=1
        if time[node]+tm > time[nd]:
            time[nd] = time[node]+tm
            parent[nd] = [node]
        elif time[node]+tm == time[nd]:
            parent[nd].append(node)
        if indeg[nd] == 0:
            q.append(nd)

check = [0]*(N+1)
answer = 0
q = deque()
q.append(end)

while q:
  node = q.popleft()
  for nd in parent[node]:
    answer += 1
    if not check[nd]:
      check[nd] = 1
      q.append(nd)
      
print(time[end])
print(answer)