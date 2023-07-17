import sys
input = sys.stdin.readline

T = int(input())
for test_case in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(9)]
    answer = 1
    
    for i in range(9):
        row = [0]*10
        column = [0]*10
        for j in range(9):
            row[board[i][j]] = 1
            column[board[j][i]] = 1

        if sum(column) != 9 or sum(row) != 9: 
            answer = 0
            break

    if answer:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                rec = [0]*10
                for dx in range(3):
                    for dy in range(3):
                        rec[board[i + dx][j + dy]] = 1

                if sum(rec) != 9:
                    answer = 0
                    break

    print('#' + str(test_case) + ' ' + str(answer))
