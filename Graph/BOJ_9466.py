import sys
input = sys.stdin.readline

for _ in range(int(input())):
  N = int(input())
  pick = [0] + list(map(int,input().split()))

  check = [0 for _ in range(N+1)]
  cnt = [0 for _ in range(N+1)]
  team = 0

  for i in range(1,N+1):
    if not check[i]:
      check[i] = i

      s = i
      c = 1
      cnt[i] = c

      while True:
        s = pick[s]

        if s == i:
          team += c
          break
        
        if not check[s]:
          check[s] = i
          c += 1
          cnt[s] = c
        elif check[s] == i:
          team += (c - cnt[s] + 1)
          break
        else:
          break

  print(N - team)