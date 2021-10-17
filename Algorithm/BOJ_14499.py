import sys
input = sys.stdin.readline
N, M, x, y, K = map(int,input().split())
dice = [[0 for _ in range(3)] for _ in range(4)]
graph = [[] for _ in range(N)]
for i in range(N):
  graph[i] = list(map(int,input().split()))
dx, dy = [0,0,0,-1,1],[0,1,-1,0,0]
move = list(map(int,input().split()))
def east():
  dice[1][0], dice[3][1], dice[1][1], dice[1][2] = dice[3][1], dice[1][2], dice[1][0], dice[1][1]
def west():
  dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[1][1], dice[1][2], dice[3][1], dice[1][0]
def north():
  dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[1][1], dice[2][1], dice[3][1], dice[0][1]
def south():
  dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[3][1], dice[0][1], dice[1][1], dice[2][1]
for j in range(K):
  if 0<=x+dx[move[j]]<N and 0<=y+dy[move[j]]<M:
    x,y = x+dx[move[j]], y+dy[move[j]]
    if move[j] == 1:
      east()
      print(dice[1][1])
    elif move[j] == 2:
      west()
      print(dice[1][1])
    elif move[j] == 3:
      north()
      print(dice[1][1])
    else:
      south()
      print(dice[1][1])
    if graph[x][y] == 0:
      graph[x][y] = dice[3][1]
    else:
      dice[3][1] = graph[x][y]
      graph[x][y] = 0