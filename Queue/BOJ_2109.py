import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N = int(input())
lecture = [[] for _ in range(10001)]
for _ in range(N):
  p, d = map(int,input().split())
  heappush(lecture[d], -p)

answer = 0
test = []
for i in range(10000,0,-1):
  for j in range(len(lecture[i])):
    heappush(test, lecture[i][j])
  if test:
    answer += heappop(test)

print(-answer)