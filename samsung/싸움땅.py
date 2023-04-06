# 02:13 02:34 (20)
# 02:47 03:30 (45)
# 03:45 05:15 (90)
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
gun_board = [[[] for _ in range(N)] for _ in range(N)]
player_board = [[-1]*N for _ in range(N)]
player_info = {}

for r in range(N):
    for c, gun in enumerate(list(map(int, input().split()))):
        if gun: gun_board[r][c].append(gun)

for i in range(M):
    x, y, d, s = map(int, input().split())
    x -= 1
    y -= 1
    player_board[x][y] = i
    player_info[i] = [x, y, d, s, 0]

def get_gun(id):
    x, y, d, s, g = player_info[id]
    if g > 0: gun_board[x][y].append(g)
    gun_board[x][y].sort()
    new_g = gun_board[x][y].pop()
    player_info[id][4] = new_g    

def fight(a_id, b_id):
    a_x, a_y, a_d, a_s, a_g = player_info[a_id]
    b_x, b_y, b_d, b_s, b_g = player_info[b_id]

    a_power = a_s + a_g
    b_power = b_s + b_g

    if a_power > b_power: return [False, a_power - b_power]
    elif a_power < b_power: return [True, b_power - a_power]
    elif a_s > b_s: return [False, 0]
    else: return [True, 0]

def lose_player(id):
    x, y, d, s, g = player_info[id]

    # 총 현재 위치에 내려놓기
    if g != 0:
        gun_board[x][y].append(g)
        player_info[id][4] = 0

    # 이동
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    for i in range(4):
        nd = d + i
        if nd >= 4: nd -= 4
        nx, ny = x + dx[nd], y + dy[nd]
        if 0 <= nx < N and 0 <= ny < N  and player_board[nx][ny] == -1:
            player_board[nx][ny] = id
            player_info[id][0], player_info[id][1], player_info[id][2] = nx, ny, nd
            if gun_board[nx][ny]: get_gun(id)
            break

def move_player(id):
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

    x, y, d, s, g = player_info[id]

    # 플레이어 이동
    nx, ny = x + dx[d], y + dy[d]
    if nx < 0 or nx >= N or ny < 0 or ny >= N: # 격자 벗어남
        if d < 2: d += 2
        else: d -= 2
        nx, ny = x + dx[d], y + dy[d]
        player_info[id][2] = d
    player_info[id][0], player_info[id][1] = nx, ny
    player_board[x][y] = -1
    
    # 이동 칸에 다른 플레이어 확인
    if player_board[nx][ny] == -1:
        player_board[nx][ny] = id
        if len(gun_board[nx][ny]) > 0: get_gun(id)
        return [-1, 0]
    else:        
        [is_win, point] = fight(player_board[nx][ny], id)

        if is_win:
            lose_player(player_board[nx][ny])
            player_board[nx][ny] = id
            if gun_board[nx][ny]: get_gun(id)
            return [id, point]
        else:
            lose_player(id)
            if gun_board[nx][ny]: get_gun(player_board[nx][ny])
            return [player_board[nx][ny], point]

def solution():
    point = [0] * M

    for _ in range(K):
        for id in range(M):
            winner_id, p = move_player(id)
            if winner_id != -1: point[winner_id] += p
            
    print(' '.join(map(str, point)))

solution()

# def solution():
#     point = [0] * M
#     print()
#     print(player_info)
#     print()
#     for i in range(N):
#         print(player_board[i])
#     for _ in range(K):
#         for id in range(M):
#             print()
#             print(id, '============================start============================')
#             print()
#             print(player_info)
#             print()
#             for i in range(N):
#                 print(player_board[i])
#             winner_id, p = move_player(id)
#             if winner_id != -1: point[winner_id] += p
#             print()
#             print('---player')
#             print(player_info)
#             print()
#             for i in range(N):
#                 print(player_board[i])
#             print()
#             print('---gun')
#             for i in range(N):
#                 print(gun_board[i])
#             print()
#             print(point) 

# solution()
