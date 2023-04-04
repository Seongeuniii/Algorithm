import sys
from collections import deque
input = sys.stdin.readline

N, Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(2**N)]
fire_storm = list(map(int, input().split()))

def rotate(L, x, y):
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    for l in range(2**(L-1)): # 감긴 횟수
        q = deque([board[x][y]])

        for _ in range(2**L - 1 - 2*l): # 길이
            x, y = x + dx[0], y + dy[0]
            q.append(board[x][y])
        
        board[x][y] = q.popleft()

        for i in range(1, 4): # 4방향
            for _ in range(2**L - 1 - 2*l): # 길이
                x, y = x + dx[i], y + dy[i]
                q.append(board[x][y])
                board[x][y] = q.popleft()

        X, Y = x, y
        
        for _ in range(2**L - 1 - 2*l - 1): # 길이
            x, y = x + dx[0], y + dy[0]
            board[x][y] = q.popleft()

        x = X + 1
        y = Y + 1

def ice():
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    minus = []

    for x in range(2**N):
        for y in range(2**N):
            if board[x][y] == 0: continue
            cnt = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < 2**N and 0 <= ny < 2**N and board[nx][ny] > 0:
                    cnt += 1
            if cnt < 3: minus.append((x, y))

    for x, y in minus:
        board[x][y] -=  1

def solution():
    a1, a2 = 0, 0
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
    check = [[0]*(2**N) for _ in range(2**N)]

    def bfs(x, y):
        ice_cnt, loc_cnt = 0, 0
        q = deque([(x, y)])

        while q:
            x, y = q.popleft()
            ice_cnt += board[x][y]
            loc_cnt += 1
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < 2**N and 0 <= ny < 2**N and not check[nx][ny] and board[nx][ny] > 0:
                    check[nx][ny] = 1
                    q.append((nx, ny))
        
        return [ice_cnt, loc_cnt]

    for x in range(2**N):
        for y in range(2**N):
            if check[x][y]: continue
            check[x][y] = 1

            if board[x][y] != 0:
                [ice_cnt, loc_cnt] = bfs(x, y)
                a1 += ice_cnt
                a2 = max(a2, loc_cnt)

    print(a1)
    print(a2)

            
for L in fire_storm:
    if L != 0:
        for x in range(0, 2**N, 2**L):
            for y in range(0, 2**N, 2**L):
                rotate(L, x, y)
    ice()

solution()