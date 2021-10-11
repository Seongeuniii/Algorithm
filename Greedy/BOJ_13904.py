import sys
from heapq import heappop,heappush
N = int(sys.stdin.readline())
hw = [[] for _ in range(1001)]
for _ in range(N):
    a,b = map(int,sys.stdin.readline().split())
    hw[a].append(b)
result = []
for i in range(1,1001):
    hw[i].sort(reverse=True)
    heappush(result,0)
    for j in hw[i]:
        test = heappop(result)
        if j >= test:
            heappush(result,j)
        else:
            heappush(result,test)
            break
print(sum(result))