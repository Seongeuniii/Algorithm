N,M = map(int,input().split())
loc = [1,M]
move = 0
J = int(input())
for _ in range(J):
  apple = int(input())
  if apple > loc[1]:
    move += apple-loc[1]
    loc = [apple-(M-1), apple]
  elif apple < loc[0]:
    move += loc[0]-apple
    loc = [apple, apple+(M-1)]
print(move)