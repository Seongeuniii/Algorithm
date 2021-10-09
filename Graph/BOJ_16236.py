import sys
from collections import deque
N = int(sys.stdin.readline())
graph = [[] for _ in range(N)]
fish = 0
for i in range(N):
    graph[i] = list(map(int,sys.stdin.readline().split()))
    for j in range(N):
        if 1<=graph[i][j]<=6:
            fish+=1
        elif graph[i][j]==9:
            graph[i][j] = 0
            srkx,srky=i,j
dx,dy = [0,0,-1,1],[-1,1,0,0]
sharksize = 2
eatfish = 0
result = 0
def bfs(sx,sy):
    global result, fish, sharksize, srkx,srky, eatfish
    visited = [[0 for _ in range(N)] for _ in range(N)]
    test = []
    mincnt = 0
    queue = deque()
    queue.append([0,sx,sy])
    visited[sx][sy] = 1
    while queue:
        c,x,y = queue.popleft()
        if mincnt !=0 and c>=mincnt:
            break
        for t in range(4):
            newx,newy = x+dx[t],y+dy[t]
            if 0<=newx<N and 0<=newy<N:
                if visited[newx][newy] == 1:
                    continue
                if graph[newx][newy]==sharksize or graph[newx][newy]==0:
                    queue.append([c+1,newx,newy])
                elif graph[newx][newy] < sharksize:
                    if mincnt == 0 or mincnt == c+1:
                        mincnt = c+1
                        test.append([mincnt,newx,newy])
                visited[newx][newy] = 1
    if len(test) == 0:
        print(result)
        sys.exit()
    test.sort(key=lambda x : (x[0], x[1], x[2]))
    result+=test[0][0]
    graph[test[0][1]][test[0][2]] = 0
    eatfish+=1
    fish -= 1
    if eatfish == sharksize:
        sharksize+=1
        eatfish = 0
    srkx,srky = test[0][1], test[0][2]
while fish>0:
    bfs(srkx,srky)
print(result)