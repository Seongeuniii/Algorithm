import sys
from heapq import heappop,heappush
input=sys.stdin.readline
T,n=map(int,input().split())
h=[]
for _ in range(n):
  A,B,C=map(int,input().split())
  heappush(h,(-C,A,B))
while h and T>0:
  T-=1
  c,a,b=heappop(h)
  print(a)
  if b-1:heappush(h,(c+1,a,b-1))