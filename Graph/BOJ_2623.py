import sys
from collections import deque
n,m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
indeg = [0 for _ in range(n+1)]
for _ in range(m):
    case = list(map(int,sys.stdin.readline().split()))
    for i in range(1,case[0]):
        graph[case[i]].append(case[i+1])
        indeg[case[i+1]] += 1
queue = deque()
for i in range(1,n+1):
    if indeg[i] == 0:
        queue.append(i)
result = []
visited = [0 for _ in range(n+1)]
while queue:
    nd = queue.popleft()
    result.append(nd)
    for l in graph[nd]:
        indeg[l] -= 1
        if indeg[l] == 0:
            queue.append(l)
if len(result) != n:
    print(0)
else:
    for k in range(n):
        print(result[k])