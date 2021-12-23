import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N,K = map(int,input().split())
P = [list(map(int,input().split())) for _ in range (N)]

answer = []
heap = []

for k in range(K):
  heappush(heap, (0,k))

for i in range(N):
  time, num = heappop(heap)
  heappush(heap, (time+P[i][1],num))
  heappush(answer,(time+P[i][1], -num, P[i][0]))

result = 0
for j in range(N):
  a,b,c = heappop(answer)
  result += (c*(j+1))
print(result)