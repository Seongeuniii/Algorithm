import sys
input = sys.stdin.readline
N = int(input())
dic = {}
for _ in range(N):
  book = input().strip()
  try:
    dic[book] += 1
  except:
    dic[book] = 1
li = list(zip(dic.keys(),dic.values()))
li.sort(key=lambda x:x[0])
li.sort(key=lambda x:x[1], reverse=True)

print(li[0][0])