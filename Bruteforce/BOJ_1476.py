E, S, M = map(int,input().split())
y = 1

while True:
  if y%15 == E%15 and y%28 == S%28 and y%19 == M%19:
    print(y)
    break
  y += 1