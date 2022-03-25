import sys
input = sys.stdin.readline

N = int(input())
info = sorted( [tuple(map(int, input().split())) for _ in range(N)] )
answer = 0
flag = False
max_height = max(info, key=lambda x:x[1])[1]

x, y = info[-1]
x += 1

while not flag:
  nx, ny = info.pop()
  if ny >= y:
    answer += ( (x-(nx+1))*y + ny )
    x, y = nx, ny

  if ny == max_height:
    info.append((nx, ny))
    flag = True

x, y = info[0]

for nx, ny in info:
  if ny >= y:
    answer += (nx-x)*y
    x, y = nx, ny

print(answer)