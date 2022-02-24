def solution(s):
  answer = len(s)
  for cut in range(1, len(s) // 2 + 1):
    result = 0
    pattern = ''
    cnt = 0
    for i in range(0, len(s), cut):
      newPattern = s[i:i+cut]
      if newPattern == pattern:
        cnt += 1
      else:
        result += len(newPattern)
        if cnt > 1:
          result += len(str(cnt))
        pattern = newPattern
        cnt = 1
    
    if cnt > 1:
      result += len(str(cnt))

    answer = min(answer, result)
  return answer