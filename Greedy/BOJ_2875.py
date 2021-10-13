import sys
N,M,K = map(int,sys.stdin.readline().split())
cnt = 0
while N-cnt*2>=0 and M-cnt*1>=0:
  if (N-cnt*2)+(M-cnt*1) >= K:
    cnt+=1
  else:
    print(cnt-1)
    sys.exit()
print(cnt-1)