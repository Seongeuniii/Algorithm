import sys
input = sys.stdin.readline
R,G,B = [0]*1001, [0]*1001, [0]*1001
N = int(input())
for i in range(1,N+1):
  r,g,b = map(int,input().split())
  R[i] = min(G[i-1], B[i-1]) + r
  G[i] = min(R[i-1], B[i-1]) + g
  B[i] = min(R[i-1], G[i-1]) + b
print(min(R[N],G[N],B[N]))