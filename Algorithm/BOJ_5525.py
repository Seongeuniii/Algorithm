N = int(input())
M = int(input())
S = input()
idx = 0
result = 0
while idx < M:
  if S[idx] == 'I':
    cnt = 1
    idx += 1
    while idx < M:
      if S[idx] != S[idx-1]:
        cnt+=1
        idx+=1
      else:
        break
    if cnt%2 == 0: cnt-= 1
    if cnt >= 2*N+1:
      result += (1+ ((cnt-(2*N+1))//2))
  else:
    idx += 1
print(result)