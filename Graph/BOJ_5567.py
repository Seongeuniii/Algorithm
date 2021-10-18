from collections import deque
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)
queue = deque()
queue.append((1,0))
visited = [0 for _ in range(n+1)]
visited[1] = 1
result = 0
while queue:
  node, cnt = queue.popleft()
  for nd in graph[node]:
    if visited[nd] == 0:
      print(node,nd)
      result+=1
      visited[nd]=1
      if cnt < 1:
        queue.append((nd,cnt+1))
print(result)