def printer():
  print(' '.join(map(str, answer)))
  
def recursive(idx, n):
  if idx == M:
    printer()
    return
    
  for i in range(n, N+1):
    if not check[i]:
      check[i] = 1
      answer[idx] = i
      recursive(idx+1, i+1)
      check[i] = 0

N, M = map(int, input().split())
check = [0]*(N+1)
answer = [0]*M

recursive(0, 1)