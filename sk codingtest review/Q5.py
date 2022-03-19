def solution(arr, processes):
    answer = []
    worktime = 0
    reqtime = [[] for _ in range(1000000)] # 요청 시간

    for process in processes:
        a, *b = process.split()
        b = list(map(int, b))
        if a == 'read':
            reqtime[b[0]].append([1] +b)
        else:
            reqtime[b[0]].append([0] +b)

    cnt = 0
    endtime = 1
    waits = reqtime[1]

    while cnt < len(processes):
        # 시작할 작업 선택
        while not waits:
            endtime += 1
            waits += reqtime[endtime]
        waits.sort(key=lambda x:(x[0],x[1]))
        w, s, m, *info =  waits[0]
        waits = waits[1:]
        cnt += 1

        if w == 1: # 읽기작업이라면
            answer.append(''.join(arr[info[0]:info[1]+1]))
            for wait in waits:
                answer.append(''.join(arr[wait[3]:wait[4]+1]))
                m = max(m, wait[2])
            cnt += len(waits) # 모든 작업들 처리
            waits = []
        else:
            for j in range(info[0], info[1]+1):
                arr[j] = str(info[2])

        worktime += m
        t = 0
        while t < m:
            t += 1
            if w == 0:
                waits += reqtime[endtime + t]
            else:
                for work in reqtime[endtime + t]:
                    if work[0] == 1 and not waits:
                        answer.append(''.join(arr[work[3]:work[4]+1]))
                        if work[1] + work[2] > endtime + m:
                            worktime += ((work[1] + work[2]-(endtime + m)))
                            m = max(m, work[1] - endtime + work[2])
                        cnt += 1
                    else:
                        waits.append(work)

        endtime += m

    answer.append(str(worktime))

    return answer

print(solution(
["1","1","1","1","1","1","1"],
["write 1 12 1 5 8","read 2 3 0 2","read 5 5 1 2","read 7 5 2 5","write 13 4 0 1 3","write 19 3 3 5 5","read 30 4 0 6","read 32 3 1 5"]
))
