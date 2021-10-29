N,M = map(int,input().split())
li = list(map(int,input().split()))
s = 0
e = max(li)
result = 0
while s<=e:
  cnt = 0
  mid = (s+e)//2
  for i in li:
    if i>mid:
      cnt += (i-mid)
  if cnt >= M:
    result = max(result,mid)
    s = mid+1
  else:
    e = mid-1
print(result)