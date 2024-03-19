import sys, math
from heapq import heappop, heappush
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))

def solution():
    wolf_dist = [[math.inf, math.inf] for _ in range(N + 1)]
    wolf_dist[1] = [math.inf, 0]
    heap = [(0, 1, 1)]

    while heap:
        t, m, w = heappop(heap)
        if wolf_dist[m][w] < t: continue

        for next_m, d in graph[m]:
            dt = d / 2 if w == 1 else d * 2
            next_w = 0 if w == 1 else 1
            if t + dt < wolf_dist[next_m][next_w]:
                wolf_dist[next_m][next_w] = t + dt
                heappush(heap, (wolf_dist[next_m][next_w], next_m, next_w))

    fox_dist = [math.inf] * (N + 1)
    fox_dist[1] = 0
    heap = [(0, 1)]

    while heap:
        t, m = heappop(heap)

        if fox_dist[m] < t: continue

        for next_m, d in graph[m]:
            if t + d < fox_dist[next_m]:
                fox_dist[next_m] = t + d
                heappush(heap, (fox_dist[next_m], next_m))

    answer = 0
    for n in range(1, N + 1):
        if fox_dist[n] < min(wolf_dist[n]):
            answer += 1

    print(answer)

solution()