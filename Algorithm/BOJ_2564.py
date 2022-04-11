import sys
input = sys.stdin.readline

W, H = map(int, input().split())
dic = {1: (0, 0, 2), 2: (H, 0, 1), 3: (0, 1, 4), 4: (W, 1, 3)}
li = []

def locate(a, b):
  if dic[a][1] == 0:  return (dic[a][0], b)
  else: return (b, dic[a][0])

for _ in range(int(input()) + 1):
  a, b = map(int, input().split())
  x, y = locate(a, b)
  li.append((a, x, y))

answer = 0
a, x, y = li.pop()

for ta, tx, ty in li:
  if ta == dic[a][2]:
    if a == 1 or a == 2: answer += (H + min(y+ty, (W-y) + (W-ty)))
    else: answer += (W + min(x+tx, (H-x) + (H-tx)))
  else: 
    answer += (abs(x-tx) + abs(y-ty))

print(answer)