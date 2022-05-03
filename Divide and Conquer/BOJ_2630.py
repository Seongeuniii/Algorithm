import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
answer = [0, 0]

def divide(x, y, l):
    color = paper[x][y]
    flag = True
    for i in range(x, x+l):
        for j in range(y, y+l):
            if paper[i][j] != color:
                flag = False
                break
    if flag:
        answer[color] += 1
    else:
        nl = l//2
        divide(x, y, nl)
        divide(x+nl, y, nl)
        divide(x, y+nl, nl)
        divide(x+nl, y+nl, nl)

divide(0, 0, N)
print(answer[0])
print(answer[1])