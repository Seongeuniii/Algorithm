import sys
from collections import deque
w, h = map(int,sys.stdin.readline().split())
while w!= 0 and h!=0:
        graph = [[] for _ in range(h)]
        for l in range(h):
            graph[l] = list(map(int,sys.stdin.readline().split()))
        dx,dy = [0,0,1,1,1,-1,-1,-1], [1,-1,0,-1,1,0,-1,1]
        def bfs(a,b):
            queue = deque()
            queue.append((a,b)) # 큐에 넣자마자 0으로 바꿔줌
            graph[b][a] = 0
            while queue:
                x, y = queue.popleft()
                for k in range(8):
                    newx = x+dx[k]
                    newy = y+dy[k]
                    if newx<0 or newx>=w or newy<0 or newy>=h:
                        continue
                    if graph[newy][newx] == 1:
                        graph[newy][newx] = 0
                        queue.append((newx,newy))
        cnt = 0
        for i in range(h):
                for j in range(w):
                    if graph[i][j] == 1:
                        cnt += 1
                        bfs(j,i)
        print(cnt)
        w, h = map(int,sys.stdin.readline().split())
