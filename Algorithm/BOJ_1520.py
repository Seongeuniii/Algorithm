import sys
sys.setrecursionlimit(10**6)
M,N = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]
dp  = [[0 for _ in range(N)] for _ in range(M)]
dp[0][0] = 1
visited  = [[0 for _ in range(N)] for _ in range(M)]
dx,dy = [0,0,-1,1], [-1,1,0,0]
def dfs(x,y):
    for i in range(4):
        newx,newy = x+dx[i], y+dy[i]
        if 0<=newx<M and 0<=newy<N:
            if graph[newx][newy] > graph[x][y]:
                if visited[newx][newy] == 0:
                    visited[newx][newy] = 1
                    dp[x][y] += dfs(newx,newy)
                else:
                    dp[x][y] += dp[newx][newy]
    return dp[x][y]
dfs(M-1,N-1)
print(dp[M-1][N-1])