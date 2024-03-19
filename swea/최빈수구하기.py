T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    score = [0]*101
    student = list(map(int, input().split()))
    answer = 0

    for s in student: score[s] += 1
    max_s = max(score)
    for i in range(100, -1, -1):
        if score[i] == max_s:
            answer = i
            break

    print('#' + str(test_case) + ' ' + str(answer))