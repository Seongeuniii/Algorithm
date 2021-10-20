import sys
input = sys.stdin.readline
R,C = map(int,input().split())
graph = [input().strip() for _ in range(R)]
dx,dy = [0,0,1,-1],[1,-1,0,0]

def bfs(a,b):
  q = {(a,b,graph[a][b])}
  check = [['' for _ in range(C)] for _ in range(R)]
  check[a][b] = graph[a][b]
  result = 1
  
  while q:
      x,y,track = q.pop()
      result = max(result,len(track))
      if result == 26:
        break

      for i in range(4):
          nx,ny = x+dx[i],y+dy[i]
          if 0<=nx<R and 0<=ny<C and graph[nx][ny] not in track and check[nx][ny] != track+graph[nx][ny]:
            check[nx][ny] = track+graph[nx][ny]
            q.add((nx,ny,check[nx][ny]))
  return result

print(bfs(0,0))

