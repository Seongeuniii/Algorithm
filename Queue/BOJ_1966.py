T = int(input())
from collections import deque
for _ in range(T):
  N,M = map(int,input().split())
  file = list(map(int,input().split()))
  li = deque()
  for i in range(N):
    li.append((i,file[i]))
  file.sort()
  cnt = 1
  b = True
  while file and b:
    idx, order = li.popleft()
    if order == file[-1]:
      if idx == M:
        b = False
        break
      else:
        file.pop()
      cnt+=1
    else: 
      li.append((idx,order))
  print(cnt)
