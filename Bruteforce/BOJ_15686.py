import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
city = []
home = []
chicken = []

for i in range(N):
  city.append(list(map(int, input().split())))
  for j in range(N):
    if city[i][j] == 1:
      home.append((i, j))
    elif city[i][j] == 2:
      chicken.append((i, j))

dist = [[] for _ in range(len(home))]

for i, (hx, hy) in enumerate(home):
  for cx, cy in chicken:
    dist[i].append(abs(hx-cx) + abs(hy-cy))

answer = []
for picks in list(combinations(range(len(chicken)), M)):
  a = 0
  for d in dist:
    t = []
    for p in picks:
      t.append(d[p])
    a += min(t)
  answer.append(a)

print(min(answer))