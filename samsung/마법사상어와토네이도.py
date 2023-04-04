import sys, math
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def sand(x, y, i):
    out = 0

    west = [(-1, 1, 0.01), 
            (1, 1, 0.01), 
            (-1, 0, 0.07),
            (1, 0, 0.07), 
            (-2, 0, 0.02),
            (2, 0, 0.02),
            (-1, -1, 0.1),
            (1, -1, 0.1),
            (0, -2, 0.05),
            (0, -1, 0)]
    east = [(x, -y, z) for x, y ,z in west]
    south = [(-y, x, z) for x, y, z in west]
    north = [(y, x, z) for x, y, z in west]

    dir = {
        0: west,
        1: south,
        2: east,
        3: north
    }

    sand_mount = board[x][y]
    curr_mount = sand_mount

    for dx, dy, rate in dir[i]:
        nx, ny = x + dx, y + dy
        move_mount = math.floor(sand_mount * rate)
        curr_mount -= move_mount

        if 0 <= nx < N and 0 <= ny < N:
            board[nx][ny] += move_mount
        else:
            out += move_mount

    dx, dy, rate = dir[i][-1]
    nx, ny = x + dx, y + dy
    if 0 <= nx < N and 0 <= ny < N:
        board[nx][ny] += curr_mount
    else:
        out += curr_mount

    board[x][y] = 0
    return out

def tornado():
    answer = 0
    dx, dy = [0, 1, 0, -1], [-1, 0, 1, 0]
    x, y = N // 2, N // 2

    for C in range(1, N, 2):
        for i in range(2):
            for _ in range(C):
                x, y = x + dx[i], y + dy[i]
                if board[x][y] == 0: continue
                answer += sand(x, y, i)
        
        for i in range(2, 4):
            for _ in range(C + 1):
                x, y = x + dx[i], y + dy[i]
                if board[x][y] == 0: continue
                answer += sand(x, y, i)

    for _ in range(N - 1):
        x, y = x + dx[0], y + dy[0]
        if board[x][y] == 0: continue
        answer += sand(x, y, 0)

    print(answer)

tornado()