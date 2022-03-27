def printer():
  print(' '.join(map(str, answer)))
  
def recursive(idx, s):
  if idx == M:
    printer()
    return
    
  for i in range(s, N):
    if cnt[li[i]]:
      cnt[li[i]] -= 1
      answer[idx] = li[i]
      recursive(idx+1, i)
      cnt[li[i]] += 1

N, M = map(int, input().split())
s = list(map(int, input().split()))

cnt = [0]*(10001)
answer = [0]*M

for l in s:
   cnt[l] += 1

li = sorted(list(set(s)))
N = len(li)

recursive(0, 0)