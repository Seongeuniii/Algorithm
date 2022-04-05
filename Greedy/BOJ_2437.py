N = int(input())
max_weight = 0

for w in sorted(list(map(int, input().split()))):
  if w <= max_weight+1:
    max_weight += w
  else:
    break
print(max_weight+1)