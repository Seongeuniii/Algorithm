import sys, copy, math
input = sys.stdin.readline

def rotate(A, idx):
    new_A = copy.deepcopy(A)
    r, c, s = rotate_info[idx]

    x = r - s
    y = c - s
    l = 0

    while (x != r and y != c):
        num = new_A[x][y]
        move = s * 2 - l * 2

        for _ in range(move):
            y += 1
            num, new_A[x][y] = new_A[x][y], num
        for _ in range(move):
            x += 1
            num, new_A[x][y] = new_A[x][y], num
        for _ in range(move):
            y -= 1
            num, new_A[x][y] = new_A[x][y], num
        for _ in range(move):
            x -= 1
            num, new_A[x][y] = new_A[x][y], num

        x += 1
        y += 1
        l += 1

    return new_A

def get_sum_of_list(A):
    s = math.inf

    for i in range(1, N + 1):
        s = min(s, sum(A[i]))

    return s

def recursive(A):
    global answer

    if (sum(is_check) == K):
        answer = min(answer, get_sum_of_list(A))

    for idx in range(K):
        if is_check[idx]: continue

        is_check[idx] = 1
        recursive(rotate(A, idx))
        is_check[idx] = 0    

N, M, K = map(int, input().split())
A = [[0] * (M + 1)]
rotate_info = []

for _ in range(N):
    A.append([0] + list(map(int, input().split())))

for _ in range(K):
    rotate_info.append(list(map(int, input().split())))

answer = math.inf
is_check = [0] * K

recursive(A)
print(answer)