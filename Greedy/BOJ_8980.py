import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N, C = map(int, input().split())
M = int(input())

send_box = [[] for _ in range(N+1)]
receive_box = [0]*(N+1)
answer = 0

for _ in range(M):
  a, b, c = map(int, input().split())
  send_box[a].append((b, c))

heap = []
for i in range(1, N+1):
  answer += receive_box[i]
  C += receive_box[i]
  receive_box[i] = 0

  for b, c in send_box[i]:
    heappush(heap, -b)
    receive_box[b] += c
    C -= c

  while C < 0:
    b = heappop(heap)
    if receive_box[-b] >= -C:
      receive_box[-b] -= (-C)
      C = 0
      heappush(heap, b)
    else:
      C += receive_box[-b]
      receive_box[-b] = 0

print(answer)