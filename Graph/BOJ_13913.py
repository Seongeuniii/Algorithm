from collections import deque 

N,K = map(int,input().split())

loc_range = 100000
check = [-1]*(2*loc_range+1)

def bfs(start):
  q = deque()
  q.append((start,0))
  check[start] = start
  if start == K:
    return 0

  while q:
    nd, cnt = q.popleft()
    if nd-1 >= 0 and check[nd-1] == -1:
      check[nd-1] = nd
      q.append((nd-1,cnt+1))
    if nd+1 <= loc_range and check[nd+1] == -1:
      check[nd+1] = nd
      q.append((nd+1,cnt+1))
    if 2*nd <= loc_range and check[2*nd] == -1:
      check[2*nd] = nd
      q.append((2*nd, cnt+1))
    
    if 2*nd == K or nd-1 == K or nd+1 == K:
      return cnt+1

def track(s):
  answer = []
  answer.append(str(s))
  while s != check[s]:
    s = check[s]
    answer.append(str(s))
  return ' '.join(answer[::-1])

print(bfs(N))
print(track(K))