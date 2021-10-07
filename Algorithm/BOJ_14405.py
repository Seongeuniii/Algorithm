import sys
S = sys.stdin.readline().strip()
S = S.replace('pi',' ')
S = S.replace('ka',' ')
S = S.replace('chu',' ')
for i in range(len(S)):
    if S[i] != ' ':
        print('NO')
        sys.exit()
print('YES')