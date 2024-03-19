from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

    def rotate():
        for c in range(N // 2):
            x, y = c, c
            q = deque()
            q.append(board[x][y])

            for n in range(N - 1 - c*2):
                x += dx[0]
                y += dy[0]
                q.append(board[x][y])

            board[x][y] = q.popleft()
            for i in range(1, 4):
                for n in range(N - 1 - c*2):
                    x += dx[i]
                    y += dy[i]
                    q.append(board[x][y])
                    board[x][y] = q.popleft()

            for _ in range(N - 2 - c*2):
                x += dx[0]
                y += dy[0]
                board[x][y] = q.popleft()

    answer = ['']*N
    for _ in range(3):
        rotate()
        for i in range(N):
            answer[i] += ' ' + ''.join(map(str, board[i]))

    print('#' + str(test_case))
    for i in range(N):
        print(answer[i][1:])