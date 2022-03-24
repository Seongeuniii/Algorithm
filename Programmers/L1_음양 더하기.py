def solution(absolutes, signs):
    answer = 0
    for i, a in enumerate(absolutes):
        if signs[i]:
            answer += a
        else:
            answer -= a        
        
    return answer