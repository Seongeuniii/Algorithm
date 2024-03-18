import sys, math
from collections import deque
input = sys.stdin.readline

N = int(input())
A, *BC = list(map(int, input().split()))
B = 0
C = 0
if (N > 1): B = BC[0]
if (N > 2): C = BC[1] 
dp = [[[math.inf] * (C + 1) for _ in range(B + 1)] for _ in range(A + 1)]

comb = [(9, 3, 1), (9, 1, 3), (3, 9, 1), (3, 1, 9), (1, 9, 3), (1, 3, 9)]
q = deque([(0, A, B, C)])
dp[A][B][C] = 0

while q:
    attack_count, _a, _b, _c = q.popleft()
    if dp[_a][_b][_c] < attack_count: continue

    for c1, c2, c3 in comb:
        a = _a - c1 if _a - c1 >= 0 else 0
        b = _b - c2 if _b - c2 >= 0 else 0
        c = _c - c3 if _c - c3 >= 0 else 0

        if (dp[a][b][c] <= attack_count + 1): continue

        dp[a][b][c] = attack_count + 1
        if a > 0 or b > 0 or c > 0: q.append((dp[a][b][c], a, b, c))

print(dp[0][0][0])
