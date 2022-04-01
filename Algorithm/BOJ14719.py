import sys
input = sys.stdin.readline

H, W = map(int, input().split())
blocks = list(map(int, input().split()))

max_height = max(blocks)
lx, max_l = 0, blocks[0]
rx, max_r = len(blocks), blocks[-1]
answer = 0

while max_l < max_height:
  lx += 1

  if blocks[lx] <= max_l:
    answer += max_l - blocks[lx]
  else:
    max_l = blocks[lx]

while max_r < max_height:
  rx -= 1
  if blocks[rx] <= max_r:
    answer += max_r - blocks[rx]
  else:
    max_r = blocks[rx]

for i in range(lx+1, rx):
  answer += (max_height-blocks[i])

print(answer)