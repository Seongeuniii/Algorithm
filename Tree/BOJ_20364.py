import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
estate = [0]*(N+1)

for _ in range(Q):
  wantedGround = int(input())
  checkground = wantedGround
  result = 0

  while checkground:
    if estate[checkground]: result = checkground
    checkground //= 2

  estate[wantedGround] = True
  print(result)