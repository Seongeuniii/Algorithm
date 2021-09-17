import sys
test = sys.stdin.readline().strip()
result = []
cnt = 0
for i in range(len(test)+1):
    if i == len(test) or test[i] != 'X':
        if cnt != 0:
            if cnt%2 != 0: # 짝수가 아니라면
                print(-1)
                sys.exit()
            else:
                result.append('AAAA'*(cnt//4))
                cnt = cnt%4
                result.append('BB'*(cnt//2))
                cnt = 0
        if i != len(test):
            result.append('.')
    else:
        cnt += 1
print(result)
for j in range(len(result)):
    print(result[j], end='')