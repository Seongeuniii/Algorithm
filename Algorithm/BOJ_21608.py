import sys
input = sys.stdin.readline

N = int(input())

# 교실 정보
room = [[0]*N for _ in range(N)]
empty = [[2] + [3]*(N-2) + [2]] + [[3] + [4]*(N-2) + [3] for _ in range(N-2)] + [[2] + [3]*(N-2) + [2]]

# 학생 정보
stdsit = [0]*(N**2+1)
stdinfo = [[] for _ in range(N**2+1)]

dx, dy = [0,0,1,-1], [1,-1,0,0]

for _ in range(N**2):
  std, *like = list(map(int,input().split()))
  stdinfo[std] = like
  
  adj = [[0]*N for _ in range(N)]
  adjPrioriy = 0
  adjStack = []

  for l in like:
    if stdsit[l]:
      x, y  = stdsit[l]
      for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<N and not room[nx][ny]:
          adj[nx][ny] += 1
          if adj[nx][ny] > adjPrioriy:
            adjPrioriy = adj[nx][ny]
            adjStack = [(empty[nx][ny], nx, ny)]
          elif adj[nx][ny] == adjPrioriy:
            adjStack.append((empty[nx][ny], nx, ny))
  
  ce, cx, cy = -1, 0, 0
  if not adjStack:
    for i in range(N):
      for j in range(N):
        if not room[i][j] and empty[i][j] > ce:
          ce = empty[i][j]
          cx, cy = i, j
  else:
    adjStack.sort(key=lambda x:(-x[0], x[1], x[2]))
    ce, cx, cy = adjStack[0]

  room[cx][cy] = std
  stdsit[std] = (cx, cy)
  for k in range(4):
    nx, ny = cx+dx[k], cy+dy[k]
    if 0<=nx<N and 0<=ny<N:
      empty[nx][ny] -= 1

answer = 0
for i in range(N):
  for j in range(N):
    s = []
    std = room[i][j]
    for k in range(4):
      ni, nj = i+dx[k], j+dy[k]
      if 0<=ni<N and 0<=nj<N:
        s.append(room[ni][nj])
    
    a = len(set(s) & set(stdinfo[std]))
    if a:
      answer += 10**(a-1)

print(answer)