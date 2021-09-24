import sys,math
from heapq import heappop,heappush
v,e,p = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(v+1)] # (거리,경로)
for i in range(e):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
heap = [] # 1번 노드부터 시작
def dijkstra(start):
    heappush(heap, (0,start))
    result[start] = 0
    while heap:
        value, nd = heappop(heap) #현재노드까지 오는 비용
        if visited[nd] == 1:
            continue
        visited[nd] = 1
        for v,n in graph[nd]: #다음 노드정보(비용,연결노드)
            if result[n] > value + v:
                result[n] = value + v
                heappush(heap, (result[n],n))
result = [math.inf for _ in range(v+1)]

visited = [0 for _ in range(v+1)]
dijkstra(1)
om = result[v] #처음부터마산까지
og = result[p] #처음부터건우까지

result = [math.inf for _ in range(v+1)]
visited = [0 for _ in range(v+1)]
dijkstra(p)
gm = result[v] #건우부터마산까지

if om >= og+gm:
    print('SAVE HIM')
else:
    print('GOOD BYE')