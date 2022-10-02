import sys, copy
input = sys.stdin.readline

def move_fish(fish_board):
    new_fish_board = copy.deepcopy(fish_board)
    fish_location = {} # key: 번호, value: 위치
    order = [] # 물고기는 번호 순서대로 이동한다. (번호, 방향)
    dx = [0, -1, -1, 0, 1, 1, 1, 0, -1] 
    dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

    for i in range(4):
        for j in range(4):
            [fish_num, fish_dir] = fish_board[i][j]
            if (0 < fish_num <= 16): 
                order.append([fish_num, fish_dir])
                fish_location[fish_num] = [i, j]

    for fish_info in sorted(order):
        [fish_num, fish_dir] = fish_info
        x, y = fish_location[fish_num]

        for idx in [i for i in range(fish_dir, 9)] + [i for i in range(1, fish_dir)]:
            nx, ny = x+dx[idx], y+dy[idx]
            if (0 <= nx < 4 and 0 <= ny < 4 and new_fish_board[nx][ny][0] != -1):
                # 현재 물고기 새로운 방향 설정
                new_fish_board[x][y][1] = idx
                # 타겟 물고기 새로운 위치 설정
                fish_location[new_fish_board[nx][ny][0]] = [x, y]
                # swap
                new_fish_board[x][y], new_fish_board[nx][ny] = new_fish_board[nx][ny], new_fish_board[x][y]
                break
    
    return new_fish_board

def move_shark(fish_board, shark_dir):
    shark_can_move_list = []
    shark_location = [-1, -1]
    dx = [0, -1, -1, 0, 1, 1, 1, 0, -1] 
    dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

    for i in range(4):
        for j in range(4):
            [fish_num, fish_dir] = fish_board[i][j]
            if (fish_num == -1): 
                shark_location = (i, j)
                break

    # 상어 이동 가능 위치
    nx, ny = shark_location
    while True:
        nx += dx[shark_dir]
        ny += dy[shark_dir]

        if (0 <= nx < 4 and 0 <= ny < 4):
            if (fish_board[nx][ny][0] > 0):
                shark_can_move_list.append((nx, ny))
        else:
            break
    
    return [shark_can_move_list, shark_location]


def recursive(ta, fish_board, shark_dir):
    global answer

    new_fish_board = move_fish(fish_board)
    [shark_can_move_list, shark_location] = move_shark(new_fish_board, shark_dir)
    (sx, sy) = shark_location
    new_fish_board[sx][sy] = [0, 0]

    for x, y in shark_can_move_list:
        [fish_num, fish_dir] = new_fish_board[x][y]
        new_fish_board[x][y] = [-1, -1]
        recursive(ta + fish_num, new_fish_board, fish_dir)
        new_fish_board[x][y] = [fish_num, fish_dir]
    
    answer = max(answer, ta)

def solution():
    global answer

    # 상어초기상태
    [fish_num, fish_dir] = fish_board[0][0]
    fish_board[0][0] = [-1, -1]
    shark_dir = fish_dir
    answer += fish_num

    # 백트래킹``
    recursive(answer, fish_board, shark_dir)
    print(answer)

answer = 0
fish_board = [[[0, 0]] * 4 for _ in range(4)] # 물고기 번호

for i in range(4):
    row = list(map(int, input().split()))
    for j in range(4):
        fish_board[i][j] = [row[2*j], row[2*j+1]] # 물고기 번호, 물고기 방향

solution()