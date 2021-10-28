K,N = map(int,input().split())
li = [int(input())for _ in range(K)]
s = 1
e = max(li)
result = 0
while s<=e:
  cnt = 0
  mid = (s+e)//2
  for i in li:
    cnt += (i//mid)
  if cnt >= N:
    result = max(result,mid)
    s = mid+1
  else:
    e = mid-1
print(result)