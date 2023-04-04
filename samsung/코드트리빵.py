import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
store = {}
distance = [[[0]*N*N for _ in range(N)] for _ in range(N)]
camp = []
people = deque()
time = 0

for i in range(M):
    r, c = map(int, input().split())
    store[i] = (r - 1, c - 1)

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            camp.append((i, j))
            continue

def calc_dist():
    dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

    for i in range(N):
        for j in range(N):
            check = [[0] * N for _ in range(N)]
            check[i][j] = 1
            q = deque([(i, j, 0)])
            
            while q:
                x, y, cnt = q.popleft()

                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    
                    if 0 <= nx < N and 0 <= ny < N and not check[nx][ny]:
                        check[nx][ny] = 1
                        if board[nx][ny] == 3: continue

                        num = nx * N + ny
                        distance[i][j][num] = cnt + 1
                        q.append((nx, ny, cnt + 1))

def move_people(t, x, y):
    dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
    store_num = store[t][0] * N + store[t][1]
    dist = 10000000000
    mx, my = 0, 0

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        
        if 0 <= nx < N and 0 <= ny < N:
            if nx == store[t][0] and ny == store[t][1]:
                board[nx][ny] = 3
                return 1
            elif board[nx][ny] == 3:
                continue  
            elif dist > distance[nx][ny][store_num]:
                dist = distance[nx][ny][store_num]
                mx, my = nx, ny

    people.append((t, mx, my))
    return 0

# t시간에 사람 한명 베이스캠프로
def get_basecamp():
    global time
    r, c = store[time - 1]
    store_num = r * N + c

    basecamp_dist = 10000000000
    br, bc = 0, 0 

    for x, y in camp:
        if board[x][y] == 3: continue
        dist = distance[x][y][store_num]
        if basecamp_dist < dist: 
            continue
        elif basecamp_dist > dist: 
            br, bc = x, y
            basecamp_dist = dist
        else:
            if br < x: continue
            elif br > x : br, bc = x, y
            elif bc < y: continue
            else: br, bc = x, y

    board[br][bc] = 3
    people.append((time - 1, br, bc))

calc_dist()
not_arrive = M

while not_arrive:
    time += 1
    p = people
    people = deque()

    while p:
        t, x, y = p.popleft()
        is_arrive = move_people(t, x, y)
        not_arrive -= is_arrive
        if is_arrive: calc_dist()
    
    if time <= M: 
        get_basecamp()
        calc_dist()

print(time)