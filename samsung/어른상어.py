import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = []
smell = [[[] for _ in range(N)] for _ in range(N)] # (time, num)
priority = [[[]] for _ in range(M + 1)]
live_shark = [] # (x, y, d)
time = 0

for r in range(N):
    board.append(list(map(int, input().split())))
    for c, num in enumerate(board[r]):
        if num > 0: 
            live_shark.append([r, c, 0]) # 방향?
            smell[r][c].append((K, num))

initial_d = [0] + list(map(int, input().split()))
for i, (x, y, _) in enumerate(live_shark):
    num = board[x][y]
    live_shark[i][2] = initial_d[num]

for i in range(4 * len(live_shark)):
    i //= 4
    priority[i + 1].append(list(map(int, input().split())))

def get_route(x, y, d):
    dx, dy = [0, -1, 1, 0, 0], [0, 0, 0, -1, 1] # 위 아 왼 오
    shark_num = board[x][y]
    no_smell = [0]*5
    my_smell = [0]*5

    for i in range(1, 5):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
        if len(smell[nx][ny]) == 0: 
            no_smell[i] = 1 # 현재 방향에 냄새 없음
        else:
            for _, num in smell[nx][ny]:
                if num == shark_num: # 상어 자신의 냄새
                    my_smell[i] = 1
                    break

    # 우선순위: 냄새 없음 -> 자기 냄새
    if sum(no_smell) > 0:
        for nd in priority[shark_num][d]: # [1,2,3,4]
            if no_smell[nd] == 1:
                return (True, nd)
    elif sum(my_smell) >= 1:
        for nd in priority[shark_num][d]: # [1,2,3,4]
            if my_smell[nd] == 1:
                return (True, nd)
    return (False, d)

def move(x, y, d):
    dx, dy = [0, -1, 1, 0, 0], [0, 0, 0, -1, 1]
    nx, ny = x + dx[d], y + dy[d]
    return (nx, ny)

# K시간 지나면 사라짐
def check_smell():
    for i in range(N):
        for j in range(N):
            li = []
            for time, num in smell[i][j]:
                if time != 1:
                    li.append((time - 1, num))
            smell[i][j] = li

def spread_smell():
    for x, y, _ in live_shark:
        num = board[x][y]
        smell[x][y].append((K, num))
          
while len(live_shark) > 1 and time <= 1000:
    time += 1

    new_board = [[0]*N for _ in range(N)]
    is_shark_alive = [0]*(M + 1)
    new_shark_info = {}

    for x, y, d in live_shark:

        shark_num = board[x][y]
        can_move, nd = get_route(x, y, d)
        nx, ny = x, y
        if can_move: nx, ny = move(x, y, nd)

        if new_board[nx][ny] == 0 or board[x][y] < new_board[nx][ny]:
            # 기존 상어 삭제
            is_shark_alive[new_board[nx][ny]] = 0

            # 새로운 상어 추가
            new_board[nx][ny] = shark_num
            is_shark_alive[shark_num] = 1
            new_shark_info[shark_num] = [nx, ny, nd]     

    new_live_shark = []
    for num in range(1, M + 1):
        if is_shark_alive[num]: new_live_shark.append(new_shark_info[num])
    
    live_shark = new_live_shark
    board = new_board

    check_smell()
    spread_smell()

if time == 1001:
    print(-1)
else:
    print(time)