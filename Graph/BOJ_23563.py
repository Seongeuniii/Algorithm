import sys, math
from heapq import heappush, heappop
input = sys.stdin.readline


H, W = map(int, input().split())
board = [list(input().strip()) for _ in range(H)]
isWall = [[0] * W for _ in range(H)]
ssx, ssy = 0, 0
eex, eey = 0, 0

def checkWall(x, y):
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    result = 0

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if nx >= 0 and nx < H and ny >= 0 and ny < W:
            if board[nx][ny] == "#":
                result = 1
                break
    
    return result

for h in range(H):
    for w in range(W):
        isWall[h][w] = checkWall(h, w)
        if board[h][w] == 'S':
            ssx, ssy = h, w
        elif board[h][w] == 'E':
            eex, eey = h, w

def dijkstra(sx, sy, ex, ey):
    dist = [[math.inf] * W for _ in range(H)]
    heap = []
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

    
    dist[sx][sy] = 0
    heappush(heap, (0, sx, sy))

    while heap:
        value, x, y = heappop(heap)
        if dist[x][y] < value: continue

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if nx >= 0 and nx < H and ny >= 0 and ny < W:
                if board[nx][ny] == "#": continue # 벽

                if isWall[x][y] and isWall[nx][ny]: # 벽타기
                    if value < dist[nx][ny]:
                        dist[nx][ny] = value
                        heappush(heap, (dist[nx][ny], nx, ny))
                else:
                    if value + 1 < dist[nx][ny]:
                        dist[nx][ny] = value + 1
                        heappush(heap, (dist[nx][ny], nx, ny))

    return dist[ex][ey]

print(dijkstra(ssx, ssy, eex, eey))