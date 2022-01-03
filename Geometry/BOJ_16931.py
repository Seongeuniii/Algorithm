import sys
input = sys.stdin.readline

N,M = map(int,input().split())
box = [[0]*(M+2)]
for _ in range(N):
  box.append([0] + list(map(int,input().split())) + [0])
box.append([0]*(M+2))

dx, dy = [0,0,1,-1], [1,-1,0,0]
answer = 0

for i in range(1,N+1):
  for j in range(1,M+1):
    answer += 2
    height = box[i][j]
    for d in range(4):
      if box[i+dx[d]][j+dy[d]] < height:
        answer += (height-box[i+dx[d]][j+dy[d]])

print(answer)