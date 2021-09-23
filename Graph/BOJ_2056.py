import sys
from collections import deque
n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
time = [0]
indeg = [0 for _ in range(n+1)]
starttime = [0 for _ in range(n+1)]
for i in range(1,n+1):
    work = list(map(int,sys.stdin.readline().strip().split()))
    time.append(work[0])
    for j in range(work[1]):
        graph[work[j+2]].append(i)
        indeg[i] += 1
queue = deque()
for k in range(1,n+1):
    if indeg[k] == 0:
        queue.append((time[k],k)) # 종료 시간
result = []
while queue:
    endtime, nd = queue.popleft() # 현재 노드 종료시간
    result.append(endtime)
    for l in graph[nd]:
        indeg[l] -= 1 # 간선 수 빼주고
        starttime[l] = max(starttime[l],endtime) # 노드의 시작 가능 시간
        if indeg[l] == 0: # 큐에 들어가지 않아도
            queue.append((starttime[l]+time[l],l))
print(max(result))