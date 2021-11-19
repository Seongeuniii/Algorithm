N = int(input())
K = int(input())
sensor = sorted(list(set(map(int,input().split()))))
li = []
for i in range(1,len(sensor)):
  li.append(sensor[i]-sensor[i-1])
li.sort()
while li and K>1:
  li.pop()
  K-=1
print(sum(li))