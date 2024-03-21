import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split()) # 직원수, 칭찬횟수
babys = [[] for _ in range(N + 1)]
boss = 0

for idx, boss_num in enumerate(list(map(int, input().split()))):
    if boss_num == -1: 
        boss = idx + 1
        continue
    babys[boss_num].append(idx + 1)

start = [0] * (N + 1)
for _ in range(M):
    i, w = map(int, input().split())
    start[i] += w

answer = [0] * (N + 1)
q = deque([boss])
while q:
    boss = q.popleft()
    for baby in babys[boss]:
        answer[baby] += (start[baby] + answer[boss])
        q.append(baby)

print(" ".join(map(str, answer[1:])))

