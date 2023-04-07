import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())
answer = 4
ladder = [[0]*(N + 1) for _ in range(H + 2)]

# 가로선 정보
for _ in range(M):
    a, b = map(int, input().split())
    ladder[a][b] = 1

def move(m, n, cnt, dots):
    global answer
    
    final_dots = dots

    for i in range(m, H + 1):
        new_dots = [k for k in range(N + 1)]
        for j in range(1, N + 1):
            v = final_dots[j]
            if ladder[i][v]: new_dots[j] = v + 1
            elif ladder[i][v-1]: new_dots[j] = v - 1
            else: new_dots[j] = v
        final_dots = new_dots

    if final_dots[1: N + 1] == [k for k in range(1, N + 1)]:
        answer = cnt

def dfs(m, n, cnt, dots):
    global answer

    if cnt >= answer: return
    elif cnt == 3:
        move(m, n, cnt, dots)
        return
        
    if m == H + 1:
        if dots[1: N + 1] == [i for i in range(1, N + 1)]:
            answer = cnt
    elif n >= N:
        # 1. 점 이동
        # 2. 다음 라인으로 이동 (m + 1, 0)
        new_dots = [i for i in range(N + 1)]
        for i in range(1, N + 1):
            v = dots[i]
            if ladder[m][v]: new_dots[i] = v + 1
            elif ladder[m][v-1]: new_dots[i] = v - 1
            else: new_dots[i] = v
        dfs(m + 1, 1, cnt, new_dots)
    else:
        # 1. 현재 라인 줄 그어주기
        # 2. n + 1
        dfs(m, n + 1, cnt, dots)
        if not ladder[m][n] and not ladder[m][n+1]:
            ladder[m][n] = 1
            dfs(m, n + 2, cnt + 1, dots)
            ladder[m][n] = 0
    return

def solution():
    dfs(1, 1, 0, [i for i in range(N + 1)])

    if answer > 3:
        print(-1)
    else:
        print(answer)

solution()