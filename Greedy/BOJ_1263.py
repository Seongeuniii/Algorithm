import sys
input = sys.stdin.readline

N = int(input())
work = [list(map(int,input().split())) for _ in range(N)]
work.sort(key=lambda x:x[1], reverse=True)
time = 0

for i in range(1,N):
  t1 = work[i-1][1]
  t2 = work[i][1]
  l = work[i-1][0]

  if t1 - t2 < l + time:
    time = (l + time) - (t1 - t2)
  else:
    time = 0

if work[N-1][1]-work[N-1][0]-time >= 0:
  print(work[N-1][1]-work[N-1][0]-time)
else:
  print(-1)