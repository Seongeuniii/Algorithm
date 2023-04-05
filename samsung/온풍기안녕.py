import sys, copy
from collections import deque
input = sys.stdin.readline

R, C, K = map(int, input().split())
board = [[0]*C for _ in range(R)]
search = [] # [(x, y)]
aircond = [] # [(방향, x, y)]

for r in range(R):
    for c, data in enumerate(list(map(int, input().split()))):
        if data == 5: search.append((r, c))
        elif 0 < data < 5: aircond.append((data, r, c))

W = int(input())
wall = [[[0]*4 for _ in range(C)] for _ in range(R)] # 오 왼 위 아: 벽 있는지

for _ in range(W):
    x, y, t = map(int, input().split())
    x -= 1
    y -= 1

    if t == 0:
        wall[x][y][2] = 1 # 위
        wall[x-1][y][3] = 1 # 아래
    else:
        wall[x][y][0] = 1 # 오
        wall[x][y+1][1] = 1 # 왼

def wind(dir, x, y):
    r_wind = [(-1, 1), (0, 1), (1, 1), (0, 1)]
    l_wind = [(x, -y) for x, y in r_wind]
    u_wind = [(-y, x) for x, y in r_wind]
    d_wind = [(y, x) for x, y in r_wind]
    r_check = [[(-1, 0, 0), (-1, 0, 3)], [(0, 0, 0)], [(1, 0, 0), (1, 0, 2)]]
    l_check = [[(-1, 0, 1), (-1, 0, 3)], [(0, 0, 1)], [(1, 0, 1), (1, 0, 2)]]
    u_check = [[(0, -1, 0), (0, -1, 2)], [(0, 0, 2)], [(0, 1, 1), (0, 1, 2)]]
    d_check = [[(0, -1, 0), (0, -1, 3)], [(0, 0, 3)], [(0, 1, 1), (0, 1, 3)]]
    way = [r_wind, l_wind, u_wind, d_wind]
    w_check = [r_check, l_check, u_check, d_check]

    check = [[0]*C for _ in range(R)]
    nx, ny = x + way[dir][-1][0], y + way[dir][-1][1]
    board[nx][ny] += 5
    check[nx][ny] = 1
    q = deque([(4, nx, ny)])

    while q:
        temp, sx, sy = q.popleft()

        # 1. 영역 안
        # 2. 중복 체크
        # 3. 벽으로 막히는지
        for i in range(3):
            nx, ny = sx + way[dir][i][0], sy + way[dir][i][1]
            if 0 <= nx < R and 0 <= ny < C and not check[nx][ny]:
                can_wind = True
                for wx, wy, w in w_check[dir][i]:
                    if wall[sx + wx][sy + wy][w]: 
                        can_wind = False
                        break
                if not can_wind: continue
                check[nx][ny] = 1
                board[nx][ny] += temp
                if temp > 1: q.append((temp - 1, nx, ny))
    
def control_temp():
    global board
    new_board = [[0]*C for _ in range(R)]
    dx, dy = [0, 0, -1, 1], [1, -1, 0, 0] # 오 왼 위 아

    for x in range(R):
        for y in range(C):
            new_board[x][y] += board[x][y]
            for i in range(4):
                if wall[x][y][i]: continue # 벽 있으면
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < R and 0 <= ny < C and board[x][y] > board[nx][ny]:
                    diff = (board[x][y] - board[nx][ny]) // 4
                    new_board[x][y] -= diff
                    new_board[nx][ny] += diff
    
    board = copy.deepcopy(new_board)

def decrease_temp():
    for c in range(C):
        if board[0][c] > 0: board[0][c] -= 1
    
    for r in range(1, R - 1):
        if board[r][0] > 0: board[r][0] -= 1
        if board[r][C-1] > 0: board[r][C-1] -= 1

    for c in range(C):
        if board[R-1][c] > 0: board[R-1][c] -= 1     

def pass_test():
    for x, y in search:
        if board[x][y] < K:
            return False
        
    return True

def solution():
    chocolate = 0

    while True:
        for dir, x, y in aircond:
            wind(dir - 1, x, y)

        control_temp()
        decrease_temp()
        chocolate += 1
        if pass_test(): break
        
        if chocolate == 100: return 101
    
    return chocolate

print(solution())