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
li = sorted(list(set(map(int, input().split()))))
N = len(li)
answer = [0]*M

recursive(0)