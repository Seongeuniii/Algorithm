import sys
sys.setrecursionlimit(10 ** 6)
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline()) 
    visited = [0 for _ in range(n)]
    li = list(map(int,sys.stdin.readline().split()))
    def dfs(n):
        if visited[n] == 0:
            visited[n] = 1
            dfs(li[n]-1)
    cnt = 0
    for k in range(n):
        if visited[k] == 0:
            cnt += 1
            dfs(k)
    print(cnt)