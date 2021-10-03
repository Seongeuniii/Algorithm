import sys
S = sys.stdin.readline().strip()
cnt = 0
while cnt<len(S):
    j = 1
    for i in range(cnt,len(S)):
        if S[i] != S[-j]:
            cnt += 1
            break
        j+=1
    if i == len(S)-1:
        break
print(len(S)+cnt)