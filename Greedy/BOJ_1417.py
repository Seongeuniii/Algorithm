import sys,math
n = int(sys.stdin.readline())
candidate = []
for _ in range(n):
    candidate.append(int(sys.stdin.readline()))
if n == 1:
    print(0)
elif n == 2:
    if candidate[0] > candidate[1]:
        print(0)
    else:
        a = candidate[1]-candidate[0]
        if a%2 == 0:
            print(a//2+1)
        else:
            print(math.ceil(a/2))
else:
    ds = candidate.pop(0)
    first = ds
    candidate.sort()
    while ds <= candidate[-1]:
        ds += 1
        candidate[-1] -= 1
        candidate.sort()
    print(ds-first)

#최대힙
import heapq
N = int(input())
q = []
D = int(input())
for _ in range(N-1):
    n = int(input())
    heapq.heappush(q, -n)
res = 0
while q:
    n = -heapq.heappop(q)
    if D > n:
        break
    D += 1
    res += 1
    heapq.heappush(q, -(n-1))
print(res)