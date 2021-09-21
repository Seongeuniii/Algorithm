import sys
sys.setrecursionlimit(10 ** 6)
n = int(sys.stdin.readline())
graph = [0 for _ in range(n+1)]
for i in range(1,n+1):
    graph[i] = int(sys.stdin.readline())
def dfs(start,now):
    visited[now] = 1
    result.append(now)
    if graph[now] == start:
        answer.extend(result)
        return
    elif visited[graph[now]] == 1:
        return
    dfs(start,graph[now])
answer = []
for j in range(1,n+1):
    result = []
    visited = [0 for _ in range(n+1)]
    if j not in answer:
        dfs(j,j)
answer.sort()
print(len(answer))
for k in range(len(answer)):
    print(answer[k])