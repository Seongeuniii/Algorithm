import sys
input = sys.stdin.readline

M, T = map(int, input().split()) # 몬스터 마리 수, 턴의 수
sx, sy = map(int, input().split()) # 팩맨 초기위치 -> 몬스터와 같을 수 있다.
sx -= 1
sy -= 1

board = [[[] for _ in range(4)] for _ in range(4)]
board_ghost = [[[] for _ in range(4)] for _ in range(4)]
egg = []

for _ in range(M):
    r, c, d = map(int, input().split()) # 위치, 방향
    r -= 1
    c -= 1
    d -= 1
    board[r][c].append(d)

# 1. 몬스터 복제 시도
def step1():
    for i in range(4):
        for j in range(4):
            for d in board[i][j]:
                egg.append((i, j, d))

# 2. 몬스터 이동
def step2():
    global board

    # 위 (왼위) 왼 (왼아) 아 (오아) 오 (오위)
    dx, dy = [-1, -1, 0, 1, 1, 1, 0, -1], [0, -1, -1, -1, 0, 1, 1, 1]
    new_board = [[[] for _ in range(4)] for _ in range(4)]

    for x in range(4):
        for y in range(4):
            for d in board[x][y]:
                is_move = False
                for i in range(8):
                    nd = d + i
                    if nd >= 8: nd -= 8
                    nx, ny = x + dx[nd], y + dy[nd]
                    # - 몬스터 시체가 있거나
                    # - 팩맨이 있거나
                    # - 격자를 벗어나거나
                    if nx == sx and ny == sy: continue
                    if 0 <= nx < 4 and 0 <= ny < 4 and len(board_ghost[nx][ny]) == 0:
                        is_move = True
                        new_board[nx][ny].append(nd)
                        break
                # 반시계 방향으로 45도씩 회전 -> 불가능하다면 움직이지 않는다.
                if not is_move: new_board[x][y].append(d)

    board = new_board

pack_path = []
max_eat = -1

# 3. 팩맨 이동
def step3():
    global sx, sy, max_eat, pack_path
    # 총 3칸 이동, (상 -> 좌 -> 하 -> 우)
    # 몬스터를 가장 많이 먹을 수 있는 방향
    # 알을 먹지 않는다.
    # 함께 있던 몬스터 먹지 않는다.
    # 몬스터 시체 그 자리에 남긴다.
    dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

    def dfs(path, eat, x, y):
        global pack_path, max_eat

        if len(path) == 3:
            if eat > max_eat:
                max_eat = eat
                pack_path = path
            return

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4:
                if (nx, ny) in path:
                    dfs(path + [(nx, ny)], eat, nx, ny)
                else:
                    dfs(path + [(nx, ny)], eat + len(board[nx][ny]), nx, ny)

    dfs([], 0, sx, sy)

    for x, y in pack_path:
        monster_cnt = len(board[x][y])
        board_ghost[x][y] += [0] * monster_cnt
        board[x][y] = []
        sx, sy = x, y
    
    pack_path = []
    max_eat = -1

# 4. 몬스터 시체 소멸
def step4():
    global board_ghost
    # 시체는 2턴 동안 유지
    new_board_ghost = [[[] for _ in range(4)] for _ in range(4)]

    for x in range(4):
        for y in range(4):
            for turn in board_ghost[x][y]:
                if turn < 2:
                    new_board_ghost[x][y].append(turn + 1)

    board_ghost = new_board_ghost

# 5. 몬스터 복제 완성
def step5():
    global egg
    # 알이었던 몬스터 부화
    for x, y, d in egg:
        board[x][y].append(d)
    egg = []

def simulate():
    for _ in range(T):
        step1()
        step2()
        step3()
        step4()
        step5()

    answer = 0
    for i in range(4):
        for j in range(4):
            answer += len(board[i][j])

    return answer

print(simulate())

# def simulate():
#     print('=============start=============', sx, sy)
#     for i in range(4):
#         print(board[i])
#     for _ in range(T):
#         step1()
#         print('----1----', sx, sy)
#         for i in range(4):
#             print(board[i])
#         step2()
#         print('----2----', sx, sy)
#         for i in range(4):
#             print(board[i])
#         step3()
#         print('----3----', sx, sy)
#         for i in range(4):
#             print(board[i])
#         step4()
#         print('----4----', sx, sy)
#         for i in range(4):
#             print(board[i])
#         step5()
#         print('----5----', sx, sy)
#         for i in range(4):
#             print(board[i])

#     answer = 0
#     for i in range(4):
#         for j in range(4):
#             answer += len(board[i][j])
        
#     return answer

# print(simulate())
