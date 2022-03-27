def printer():
  print(' '.join(map(str, answer)))

def recursive(idx, n):
  if idx == M:
    printer()
    return

  for i in range(n, N+1):
    answer[idx] = i
    recursive(idx+1, i)

N, M = map(int, input().split())
answer = [0]*M

recursive (0, 1)