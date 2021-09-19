import sys
from collections import deque
t = int(sys.stdin.readline())
for _ in range(t):
    l = int(sys.stdin.readline()) #체스판 한변의 길이
    nowx, nowy = map(int,sys.stdin.readline().split())
    afterx, aftery = map(int,sys.stdin.readline().split())

    dx = [-2,-2,-1,-1,+1,+1,+2,+2]
    dy = [+1,-1,+2,-2,+2,-2,+1,-1]

    visited = [[0 for _ in range(l)] for _ in range(l)]
    queue = deque()
    queue.append((0,nowx,nowy))
    cnt = 0
    while queue:
        cnt,x,y = queue.popleft()
        if x == afterx and y == aftery:
            break
        visited[x][y] = 1
        for i in range(8):
            newx, newy = x+dx[i], y+dy[i]
            if newx < 0 or newx >= l or newy < 0 or newy >= l:
                continue
            if visited[newx][newy] == 0:
                queue.append((cnt+1,newx,newy))
                visited[newx][newy] = 1
    print(cnt)