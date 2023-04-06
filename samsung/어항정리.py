import sys
input = sys.stdin.readline

N, K = map(int, input().split())
board = [list(map(int ,input().split()))] + [[0] * (N) for _ in range(N - 1)]
count = [1] * N

def add_fish():
    min_cnt = min(board[0])
    for idx, fish in enumerate(board[0]):
        if fish == min_cnt: board[0][idx] += 1

def move_left_one():
    lx = 0
    ly = 0
    rx = 0
    ry = ly + 1

    fish = board[lx][ly]
    board[rx + 1][ry] = fish # 오른쪽 어항 위로 올리기
    board[lx][ly] = 0

    count[ly] -= 1
    count[ry] += 1

def rotate1():
    while True:
        # 2개 이상 개수
        start = -1
        over_two = 0
        for idx, c in enumerate(count):
            if c > 1: 
                over_two += 1
                if start == -1: start = idx
        
        # 겹쳤을 때 튀어나오면 안됨
        if over_two > 0 and count[start] <= N - start - over_two:
            lx = 0
            ly = start + over_two

            for dy in range(1, over_two + 1):
                sx = lx
                sy = ly - dy
                fish = board[sx][sy]
                board[lx + dy][ly] = fish # 위로 올리기
                board[sx][sy] = 0
            
                for dx in range(1, count[start]):
                    mx = sx + dx
                    my = sy
                    fish = board[mx][my]
                    board[lx + dy][ly + dx] = fish # 오른쪽으로 나열
                    board[mx][my] = 0

            l = count[start]
            for i in range(ly):
                count[i] = 0
            for i in range(ly, ly + l):
                count[i] += over_two

        else:
            break

def control_fish():
    global board
    new_board = [[0]*N for _ in range(N)]
    dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

    for x in range(N):
        for y in range(N):
            if board[x][y] == 0: continue
            new_board[x][y] += board[x][y]
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < N and 0 <= ny < N and board[nx][ny] > 0 and board[x][y] > board[nx][ny]:
                    value = (board[x][y] - board[nx][ny]) // 5
                    if value > 0:
                        new_board[x][y] -= value
                        new_board[nx][ny] += value

    board = new_board

def reset_board():
    global count
    line = [0]*N
    idx = 0
    for y in range(N):
        for x in range(N):
            if board[x][y] == 0: break
            line[idx] = board[x][y]
            board[x][y] = 0
            idx += 1

    board[0] = line
    count = [1] * N

def rotate2():
    lx = 0
    ly = 0

    for i in range(N // 2):
        fish = board[0][ly + i]
        board[1][N - i - 1] = fish
        board[0][ly + i] = 0
    
    ly  = N // 2

    for i in range(N // 2 // 2):
        fish = board[1][ly + i]
        board[2][N - i - 1] = fish
        board[1][ly + i] = 0

        fish = board[0][ly + i]
        board[3][N - i - 1] = fish
        board[0][ly + i] = 0


def solution():
    answer = 0

    while True:
        min_fish = min(board[0])
        max_fish = max(board[0])

        if max_fish - min_fish <= K: break
        answer += 1

        add_fish()
        move_left_one()
        rotate1()
        control_fish()
        reset_board()
        rotate2()
        control_fish()
        reset_board()
    
    return answer

print(solution())