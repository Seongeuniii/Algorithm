import sys, math
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
sx, sy = 0, 0
mannequin = deque()

for n in range(N):
    for m in range(M):
        if board[n][m] == 3:
            board[n][m] = 1
            mannequin.append((n, m))
        elif board[n][m] == 4:
            sx, sy = n, m

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def cannot_go(q):
    dist = [[math.inf] * M for _ in range(N)]

    for x, y in mannequin: dist[x][y] = 0
            
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if dist[nx][ny] > dist[x][y] + 1:
                    dist[nx][ny] = dist[x][y] + 1
                    board[nx][ny] = 1
                    if dist[nx][ny] < K:
                        q.append((nx, ny))

def find_bench(sx, sy):
    check = [[0] * M for _ in range(N)]
    check[sx][sy] = 1
    q = deque([(sx, sy, 0)])

    while q:
        x, y, d = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < M and not check[nx][ny] and board[nx][ny] != 1:
                if board[nx][ny] == 2:
                    return d + 1
                check[nx][ny] = 1
                q.append((nx, ny, d + 1))

    return -1

if K > 0: cannot_go(mannequin)
print(find_bench(sx, sy))