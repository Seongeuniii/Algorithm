from itertools import permutations

def solution(k, dungeons):
    answer = 0 
    
    for case in list(permutations(dungeons, len(dungeons))):
        p = k
        cnt = 0
        for c in case:
            if c[0] <= p:
                p -= c[1]
                cnt += 1
            else:
                break
                
        answer = max(answer, cnt)
        
    return answer