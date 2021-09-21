import sys
from heapq import heappop,heappush
n = int(sys.stdin.readline())
li = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(li) == 0:
            print(0)
        else:
            print(-heappop(li))
    else:
        heappush(li,-x)