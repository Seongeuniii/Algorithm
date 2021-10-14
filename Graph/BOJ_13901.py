R,C = map(int,input().split())
graph = [[0 for _ in range(C)] for _ in range(R)]
k = int(input())
for _ in range(k):
  br,bc = map(int,input().split())
  graph[br][bc] = 1
sr,sc = map(int,input().split())
graph[sr][sc] = 1
move = list(map(int,input().split()))
idx = 0
dx,dy = [-1,1,0,0],[0,0,-1,1]
queue = []
queue.append((sr,sc))
while queue:
  rr,rc = queue.pop()
  for _ in range(4):
    newx, newy = rr+dx[move[idx]-1],rc+dy[move[idx]-1]
    if 0<=newx<R and 0<=newy<C:
      if graph[newx][newy] == 0:
        graph[newx][newy] = 1
        queue.append((newx,newy))
        break
    if idx==3:
      idx=0
    else:
      idx+=1
print(rr,rc)