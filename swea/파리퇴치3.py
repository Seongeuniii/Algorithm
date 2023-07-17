import sys
input = sys.stdin.readline

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    dx, dy = [0, 0, 1, -1, -1, -1, 1, 1], [1, -1, 0, 0, -1, 1, -1, 1]
    answer = 0

    for cx in range(N):
        for cy in range(N):
            cnt = [0] * 8
            for i in range(8):
                x = cx
                y = cy
                for _ in range(M - 1):
                    x += dx[i]
                    y += dy[i]
                    if 0 <= x < N and 0 <= y < N: cnt[i] += board[x][y]
                    else: break

            center = board[cx][cy]
            answer = max(answer, center + sum(cnt[:4]), center + sum(cnt[4:]))

    print('#' + str(test_case) + ' ' + str(answer))
