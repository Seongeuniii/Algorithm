import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
indeg = [0] * (N + 1)
route = [[0, 0] for _ in range(N + 1)]

for _ in range(M):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    indeg[q] += 1


q = deque([1])
indeg[1] = 0
while q:
    node = q.popleft()
    value = route[node][0]

    for nd, v in graph[node]:
        if route[nd][0] < value + v:
            route[nd] = [value + v, node]
        indeg[nd] -= 1
        if indeg[nd] == 0:
            q.append(nd)

last_node = route[1][1]
answer = [1, last_node]
while last_node != 1:
    last_node = route[last_node][1]
    answer.append(last_node)
print(route[1][0])
print(" ".join(map(str, reversed(answer))))