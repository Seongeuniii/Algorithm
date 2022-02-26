def solution(s):
    answer = []
    s = s[2:-2].split('},{')
    
    for i in range(len(s)):
      s[i] = list(map(int,s[i].split(',')))

    for li in sorted(s, key=len):
        for l in li:
          if l not in answer:
            answer.append(l)

    return answer

print(solution('{{2},{2,1},{2,1,3},{2,1,3,4}}'))