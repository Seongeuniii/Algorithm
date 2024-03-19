import sys
from heapq import heappop, heappush
input = sys.stdin.readline

max_heap = [] 
min_heap = []
remain = [[1, 0] for _ in range(100001)] 

N = int(input())
for _ in range(N):
    P, L = map(int, input().split()) # 번호 난이도
    remain[P][1] = 1
    heappush(max_heap, (-L, -P, 1))
    heappush(min_heap, (L, P, 1))
M = int(input())
for _ in range(M):
    cmd, *a = list(input().split())
    num = list(map(int, a))

    if cmd == "recommend":
        if num[0] == 1:
            while True:
                l, p, v = heappop(max_heap)
                if remain[-p][0] == v and remain[-p][1]:
                    print(-p)
                    heappush(max_heap, (l, p, v))
                    break
        else:
            while True:
                l, p, v = heappop(min_heap)
                if remain[p][0] == v and remain[p][1]:
                    print(p)
                    heappush(min_heap, (l, p, v))
                    break
    elif cmd == "add":
        P, L = num
        nv = remain[P][0] + 1
        remain[P] = [nv, 1]
        heappush(max_heap, (-L, -P, nv))
        heappush(min_heap, (L, P, nv))
    elif cmd == "solved":
        remain[num[0]][1] = 0