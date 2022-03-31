import sys, math
input = sys.stdin.readline

N, M, B = map(int, input().split())
ground = []
blocks = [0]*257
answer = [math.inf, 0]

for i in range(N):
  ground.append(list(map(int, input().split())))
  for j in range(M):
    blocks[ground[i][j]] += 1

for h in range(257):
  plus = 0
  minus = 0

  for i in range(257):
    if i > h:
      minus += (i-h)*(blocks[i])
    else:
      plus += (h-i)*(blocks[i])
  
  if minus + B >= plus and answer[0] >= minus*2 + plus:
    answer = [minus*2 + plus, h]

print(answer[0], answer[1])