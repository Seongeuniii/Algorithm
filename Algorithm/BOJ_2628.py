import sys
input = sys.stdin.readline

W, H = map(int,input().split())
N = int(input())
wli = [0,H]
hli = [0,W]

for _ in range(N):
  a, b = map(int,input().split())
  if a == 0:
    wli.append(b)
  else:
    hli.append(b)

wli.sort()
hli.sort()

w, h = 0, 0
for i in range(1,len(wli)):
  w = max(w, wli[i] - wli[i-1])
for i in range(1,len(hli)):
  h = max(h, hli[i] - hli[i-1])

print(w*h)