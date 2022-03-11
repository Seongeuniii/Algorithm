import sys
input = sys.stdin.readline

N = int(input())
li = sorted([int(input()) for _ in range(N)])

print(round(sum(li)/N))

print(li[int(N/2)])

dic = {}
for l in li:
  try: dic[l] += 1
  except: dic[l] = 1
a = sorted(list(dic.items()), key=lambda x:(-x[1], x[0]))

if len(a) >= 2 and a[0][1] == a[1][1]:
  print(a[1][0])
else:
  print(a[0][0])

print(max(li) - min(li))