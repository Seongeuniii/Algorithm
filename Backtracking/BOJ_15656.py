def printer():
  print(' '.join(map(str, answer)))
  
def recursive(idx):
  if idx == M:
    printer()
    return
    
  for i in range(N):
    answer[idx] = li[i]
    recursive(idx+1)

N, M = map(int, input().split())
li = sorted(list(map(int, input().split())))
answer = [0]*M

recursive(0)