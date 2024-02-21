import sys
from collections import deque
input =  sys.stdin.readline

N, M = map(int, input().split())
graph = [{} for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v] = True
    graph[v][u] = True

answer = -1
checked = [0] * (N + 1)

def bfs(node):
    cut_count = 0
    q = deque([(-1, node)])
    checked[node] = 1

    while q:
        bn, n = q.popleft()

        for nn, connected in graph[n].items():
            if nn == bn or not connected: continue
            
            if checked[nn]:
                cut_count += 1
                graph[n][nn] = False
                graph[nn][n] = False
            else:
                checked[nn] = 1
                q.append((n, nn))
    
    return cut_count

for i in range(1, N + 1):
    if not checked[i]:
        answer += 1
        answer += bfs(i)

print(answer)

