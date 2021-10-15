import sys,math
from collections import deque
N = int(input()) # 보드 크기
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
K = int(input()) # 사과 위치
for _ in range(K):
  aa,ab = map(int,input().split())
  graph[aa][ab] = 2
tail = deque()
tail.append((1,1))
dic = {'RR':0, 'LL':1, 'UU':2, 'DD':3}
drc = 'RR'
x,y,graph[1][1] = 1,1,1
dx,dy = [0,0,-1,1],[1,-1,0,0]
L = int(input()) # 방향 전환
cnt = 0
case = deque()
for _ in range(L):
  ca,cb = input().split()
  case.append((ca,cb))
case.append((20000,''))
while case:
  time,newdrc = case.popleft()
  for _ in range(int(time)-cnt):
    cnt+=1
    newx,newy = x+dx[dic[drc]], y+dy[dic[drc]]
    if 0<newx<=N and 0<newy<=N and graph[newx][newy] != 1:
      if graph[newx][newy] != 2:
        a,b = tail.popleft()
        graph[a][b] = 0 # 꼬리 빠짐
      tail.append((newx,newy))
      graph[newx][newy] = 1
      x,y = newx,newy
    else:
      print(cnt)
      sys.exit()
  if newdrc == 'L': #왼쪽
    if drc == 'RR':
      drc = 'UU'
    elif drc == "LL":
      drc = "DD"
    elif drc == "DD":
      drc = "RR"
    else:
      drc = "LL"
  else: #오른쪽
    if drc == 'RR':
      drc = 'DD'
    elif drc == "LL":
      drc = "UU"
    elif drc == "DD":
      drc = "LL"
    else:
      drc = "RR"
print(cnt)
    
