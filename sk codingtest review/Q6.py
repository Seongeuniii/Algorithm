def solution(goods):
    answer = []
  
    def find(good, s):
        for othergood in goods:
            if othergood == good:
                continue
            if s in othergood:
                return 0
        return 1

    for idx, good in enumerate(goods):
        result = set()
        for i in range(1, len(good)+1):
            for j in range(len(good)-i+1):
                s = good[j:j+i]
                if find(good, s):
                    result.add(s)

            if result:  
                answer.append(' '.join(sorted(list(result))))
                break
            
        if len(answer) < idx + 1:
            answer.append('None')

    return answer