from collections import deque

S = int(input())
check = [[0]*(S+1)for _ in range(S+1)]

def bfs(start):
  q = deque()
  q.append((start,0,0))
  check[1][0] = 1

  while q:
    num, clip, cnt = q.popleft()

    if num and not check[num][num]:
      check[num][num] = 1
      q.append((num,num,cnt+1))

    if clip and num+clip<=S and not check[num+clip][clip]:
      check[num+clip][clip] = 1
      q.append((num+clip,clip,cnt+1))

    if num and not check[num-1][clip]:
      check[num-1][clip] = 1
      q.append((num-1,clip,cnt+1))

    if num+clip == S or num-1 == S:
      return cnt + 1

print(bfs(1))