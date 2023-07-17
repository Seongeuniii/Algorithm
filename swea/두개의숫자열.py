import sys
input = sys.stdin.readline

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if N > M:
        N, M = M, N
        A, B = B, A

    answer = 0

    for i in range(M - N + 1):
        c = 0
        for j in range(N):
            c += A[j] * B[i + j]
        answer = max(answer, c)

    print('#' + str(test_case) + ' ' + str(answer))
