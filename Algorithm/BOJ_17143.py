import sys
input = sys.stdin.readline

answer = 0
R, C, M = map(int,input().split())
sea = [[0]*(C+1) for _ in range(R+1)]
shark = [0]*10001
p = 0
rWay = {0: 1, 1: 0, 2: 3, 3: 2 }
dx, dy = [-1,1,0,0], [0,0,1,-1]

for _ in range(M):
  r, c, s, d, z = map(int,input().split())
  sea[r][c] = z
  shark[z] = (s, d-1)

while p < C:
  p += 1
  
  for r in range(1, R+1):
    if sea[r][p]:
      answer += sea[r][p]
      sea[r][p] = 0
      break
  
  if p == C:
    break
  
  newSea = [[0]*(C+1) for _ in range(R+1)]
  for r in range(1, R+1):
    for c in range(1, C+1):
      if sea[r][c]:
        z = sea[r][c]
        x, y = r, c
        s, d = shark[z]
        ss = s 
        if d == 0 or d == 1:
          s %= ((R-1)*2)
        else:
          s %= ((C-1)*2)
        for _ in range(s):
          nx, ny = x+dx[d], y+dy[d]
          if 0<nx<=R and 0<ny<=C:
            x, y = nx, ny
          else:
            d = rWay[d]
            x, y = x+dx[d], y+dy[d]
        
        if newSea[x][y] < z:
          newSea[x][y] = z
          shark[z] = (ss, d)
  
  sea = newSea
  
print(answer)