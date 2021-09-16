import sys
sys.setrecursionlimit(10 ** 6)
n = int(sys.stdin.readline())
a, b = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int,sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0 for _ in range(n+1)]
def dfs(cnt, n):
    global b, result
    cnt += 1
    visited[n] = 1
    for l in graph[n]:
        if l == b:
            print(cnt)
            sys.exit()
        if visited[l] == 0:
            dfs(cnt, l)

dfs(0, a)
print(-1)