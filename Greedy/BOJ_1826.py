import sys
from heapq import heappop,heappush
input = sys.stdin.readline
N = int(input())
gas = [0 for _ in range(1000001)]
for _ in range(N):
  a,b = map(int,input().split())
  gas[a] = b
L,P = map(int,input().split())
q = []
loc = 0
move = P
cnt = 0
while loc < L:
  if loc != 0:
    if q:
      move = (-heappop(q)+loc)
      cnt += 1
    else:
      print(-1)
      sys.exit()
  for i in range(loc+1,move+1):
    if i > L: break
    if gas[i]: heappush(q,-gas[i])
  loc = move
print(cnt)