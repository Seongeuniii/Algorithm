import sys, math
from heapq import heappush, heappop
input = sys.stdin.readline

def dijkstra(start, end):
    dist = [math.inf]*(N+1)
    heap = []

    dist[start] = 0
    heappush(heap, (0, start))

    while heap:
        w, node = heappop(heap)

        if dist[node] < w: continue

        for nd, v in enumerate(graph[node]):
            if v == 0: continue

            if w + v < dist[nd]:
                dist[nd] = w + v
                heappush(heap, (dist[nd], nd))

    return dist[end]


N, M = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

s, t = map(int, input().split())
answer = dijkstra(s, t)
print(answer)
