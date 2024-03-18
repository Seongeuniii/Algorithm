import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
sushi_order_q = [deque() for _ in range (200001)]
answer = [0] * (N)

for n in range(N):
    K, *order_list = list(map(int, input().split()))

    for menu in order_list:
        sushi_order_q[menu].append(n)

for sushi in list(map(int, input().split())):
    if not sushi_order_q[sushi]: continue
    
    eat = sushi_order_q[sushi].popleft()
    answer[eat] += 1

print(' '.join(map(str, answer)))