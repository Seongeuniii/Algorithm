from collections import deque

R, C = map(int, input().split())
check = [[0]*(C+1) for _ in range(R+1)]
cnt = [[0]*(C+1) for _ in range(R+1)]
dx, dy = [-2,-2,2,2,-1,1,-1,1], [-1,1,-1,1,2,2,-2,-2]

check[1][1] = 1
cnt[1][1] = 1
q = deque([(1,1)])
t = 1

while q:
  t += 1
  dq = q
  q = deque()

  while dq:
    x, y = dq.popleft()
    for i in range(8):
      nx, ny = x+dx[i], y+dy[i]
      if 0<nx<=R and 0<ny<=C:
        if not check[nx][ny]:
          check[nx][ny] = t
          cnt[nx][ny] = cnt[x][y]
          q.append((nx, ny))
        elif check[nx][ny] == t:
          cnt[nx][ny] += cnt[x][y]

if not cnt[R][C]:
  print('None')
else:
  print(check[R][C]-1, cnt[R][C]%1000000009)