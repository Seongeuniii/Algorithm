import math
from heapq import heappush, heappop

def solution(n, s, a, b, fares):
    def dijkstra(start):
        dist = [math.inf]*(n+1)
        heap = []
        
        dist[start] = 0
        heappush(heap, (0, start))

        while heap:
            value, node = heappop(heap)
            if dist[node] < value: continue

            for v, nd in graph[node]:
                if value + v < dist[nd]:
                    dist[nd] = value + v
                    heappush(heap, (dist[nd], nd))

        return dist
    
    graph = [[] for _ in range(n+1)]

    for c, d, f in fares:
        graph[c].append((f, d))
        graph[d].append((f, c))
        
    dist_a = dijkstra(a)
    dist_b = dijkstra(b)
    dist_s = dijkstra(s)
    
    answer = math.inf
    for i in range(1, n+1):
        answer = min(answer, dist_s[i] + dist_a[i] + dist_b[i])
    
    return answer