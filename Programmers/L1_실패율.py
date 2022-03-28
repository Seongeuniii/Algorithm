def solution(N, stages):
    step = [0]*(N+2)
    fail =  []
    answer= []
    
    for stage in stages:
        step[stage] += 1
        
    upstage = step[N+1]
    
    for i in range(N, 0, -1):
        upstage += step[i]
        if not upstage:
            fail.append((0, i))
        else:
            fail.append((step[i] / upstage, i))
    
    for f, n in sorted(fail, key=lambda x:(-x[0], x[1])):
        answer.append(n)
    
    return answer