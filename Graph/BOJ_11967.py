# case1
from sys import stdin
from collections import deque
N,M = map(int,stdin.readline().split())
room_sw = [[[] for _ in range(N+1)] for _ in range(N+1)]
s_on = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    x,y,a,b = map(int,stdin.readline().split())
    room_sw[x][y].append((a,b))
dx,dy = [0,0,1,-1],[1,-1,0,0]
queue = deque()
def bfs(rx,ry):
    visited = [[0 for _ in range(N+1)] for _ in range(N+1)]
    news_on = []
    queue.append((rx,ry))
    visited[rx][ry] = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            newx,newy = x+dx[i],y+dy[i]
            if newx<=0 or newx>N or newy<= 0 or newy>N:
                continue
            if s_on[newx][newy] == 1 and visited[newx][newy] == 0:
                visited[newx][newy] = 1
                queue.append((newx,newy))
                if s_on[newx][newy] == 0:
                    s_on[newx][newy] = 1
                    for a,b in room_sw[newx][newy]:
                        news_on.append((a,b))
    return news_on
cnt = 1
s_on[1][1] = 1
for a,b in room_sw[1][1]:
    if s_on[a][b] == 0:    
        s_on[a][b] = 1
        cnt += 1
move = True
while move:
    move = False
    news_on = bfs(1,1)
    if news_on:
        for a,b in news_on:
            if s_on[a][b] == 0:
                s_on[a][b] = 1
                cnt += 1
                move = True
print(cnt)

# case2
from sys import stdin
from collections import deque
N,M = map(int,stdin.readline().split())
room_sw = [[[] for _ in range(N+1)] for _ in range(N+1)]
s_on = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    x,y,a,b = map(int,stdin.readline().split())
    room_sw[x][y].append((a,b))
dx,dy = [0,0,1,-1],[1,-1,0,0]
def turnon(startx,starty):
    s_on[startx][starty], visited[startx][starty], cnt = 1, 1, 1
    queue = deque()
    queue.append((startx,starty))    
    while queue:
        x,y = queue.popleft()
        for a,b in room_sw[x][y]:
            if s_on[a][b] == 0:
                s_on[a][b] = 1
                cnt += 1
                for i in range(4): 
                    ax,by = a+dx[i],b+dy[i]
                    if 0<ax<=N and 0<by<=N and visited[ax][by]:
                        queue.append((ax,by))
                        break
        for i in range(4):
            rx,ry = x+dx[i],y+dy[i]
            if 0<rx<=N and 0<ry<=N and s_on[rx][ry] and not visited[rx][ry]:
                visited[rx][ry] = 1
                queue.append((rx,ry))
    return cnt
print(turnon(1,1))