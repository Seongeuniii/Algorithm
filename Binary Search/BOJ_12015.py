# N = int(input())
# li = list(map(int,input().split()))
# x = [0]
# for i in range(N):
#   if li[i] > x[-1]:
#     x.append(li[i])
#     continue

#   s = 1
#   e = len(x)
#   while s <= e:
#     mid = (s+e)//2
#     if x[mid] == li[i]:
#       break
#     elif x[mid] > li[i]:
#       e = mid - 1
#     else:
#       s = mid + 1
  
#   if x[mid] < li[i]:
#     x[mid+1] = li[i]
#   else:
#     x[mid] = li[i]

# print(len(x)-1)

N = int(input())
li = list(map(int,input().split()))
x = [0]
for l in li:
  if l > x[-1]:
    x.append(l)
    continue

  s = 0
  e = len(x)
  while s < e:
    mid = (s+e)//2
    if x[mid] < l:
      s = mid + 1
    else:
      e = mid
  x[e] = l

print(len(x)-1)