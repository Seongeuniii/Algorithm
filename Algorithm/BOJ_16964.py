import sys
from collections import deque
input = sys.stdin.readline

q = [0] + [deque(list(map(int, input().strip()))) for _ in range(4)]
order = [tuple(map(int, input().split())) for _ in range(int(input()))]

for num, dir in order:
  cycle = [0]*5
  cycle[num] = dir
  
  tn = num
  while tn > 1:
    tn -= 1
    if q[tn][2] != q[tn+1][6]:
      if cycle[tn+1] == 1:
        cycle[tn] = -1
      else:
        cycle[tn] = 1
    else:
      break

  tn = num
  while tn < 4:
    tn += 1
    if q[tn][6] != q[tn-1][2]:
      if cycle[tn-1] == 1:
        cycle[tn] = -1
      else:
        cycle[tn] = 1
    else:
      break

  for i in range(1, 5):
    if cycle[i] == 1:
      q[i].appendleft(q[i].pop())
    elif cycle[i] == -1:
      q[i].append(q[i].popleft())

score = 0
for i in range(1, 5):
  if q[i][0] == 1:
    score +=  2**(i-1)

print(score)