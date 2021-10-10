import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    graph = [[] for _ in range(n+1)]
    indeg = [0 for _ in range(n+1)]
    last = list(map(int,input().split()))
    for i in range(0,n-1):
        for j in range(i+1,n):
            graph[last[i]].append(last[j])
            indeg[last[j]]+=1
    m = int(input())
    for _ in range(m):
        a,b = map(int,input().split())
        if a in graph[b]:
            graph[b].remove(a)
            graph[a].append(b)
            indeg[a]-=1
            indeg[b]+=1
        else:
            graph[a].remove(b)
            graph[b].append(a)
            indeg[b]-=1
            indeg[a]+=1
    rank = True
    result = []
    node = deque()
    for k in range(1,n+1):
        if indeg[k] == 0:
            node.append(k)
    while node:
        if len(node)>1:
            rank = False
        nd = node.popleft()
        result.append(nd)
        for nd in graph[nd]:
            indeg[nd]-=1
            if indeg[nd] == 0:
                node.append(nd)
    if len(result) != n:
        print('IMPOSSIBLE')
    elif rank == False:
        print('?')
    else:
        for l in range(n-1):
            print(result[l],end=' ')
        print(result[n-1])