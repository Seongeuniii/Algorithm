def printer():
  print(' '.join(map(str, answer)))
  
def recursive(idx):
  if idx == M:
    printer()
    return
    
  for l in li:
    if cnt[l]:
      cnt[l] -= 1
      answer[idx] = l
      recursive(idx+1)
      cnt[l] += 1

N, M = map(int, input().split())
s = list(map(int, input().split()))
cnt = [0]*(10001)
answer = [0]*M

for l in s:
   cnt[l] += 1
li = sorted(list(set(s)))
recursive(0)