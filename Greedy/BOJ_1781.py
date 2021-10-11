import sys
from heapq import heappop,heappush
N = int(sys.stdin.readline())
dline = [[] for _ in range(N+1)]
for _ in range(N):
    a,b = map(int,sys.stdin.readline().split())
    dline[a].append(b)
result = []
for i in range(1,N+1):
    dline[i].sort(reverse=True) #최댓값
    heappush(result,0)
    for j in dline[i]:
        test = heappop(result) # 최솟값
        if j >=test:
            heappush(result, j)
        else:
            heappush(result, test)
            break
print(sum(result))