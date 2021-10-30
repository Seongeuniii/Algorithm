N = int(input())
city = list(map(int,input().split()))
M = int(input())
s = 1
e = max(city)
result = 0
while s<=e:
  value = 0
  mid = (s+e)//2
  for i in city:
    if i >= mid:
      value += mid
    else:
      value += i
  if value <= M:
    result = max(result,mid)
    s = mid+1
  else:
    e = mid-1
print(result)