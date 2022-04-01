import sys

input = sys.stdin.readline

def floydWarshall():
  for k in range(1, N+1):
    for i in range(1, N+1):
      for j in range(1, N+1):
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

N = int(input())
dist = [[100]*(N+1) for _ in range(N+1)]

while True:
  a, b = map(int, input().split())
  if  a == -1 and b == -1:
    break
  dist[a][b] = 1
  dist[b][a] = 1

for i in range(N+1):
  dist[i][i] = 0

floydWarshall()

cdd = []
score = 100

for i in range(1, N+1):
  scr = max(dist[i][1:])

  if scr < score:
    score = scr
    cdd = [i]
  elif scr == score:
    cdd.append(i)


print(score, len(cdd))
print(' '.join(map(str, cdd)))