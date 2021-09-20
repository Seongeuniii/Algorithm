import sys
n = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))
alpha = {}
for i in range(n):
    if num[i] == 0:
        a = ' '
    elif 27<=num[i]<=52:
        a = chr(num[i]+70)
    else:
        a = chr(num[i]+64)
    try:
        alpha[a]+= 1
    except:
        alpha[a] = 1

code = sys.stdin.readline().strip()

for j in range(n):

    if code[j] in alpha and alpha[code[j]] > 0:
        alpha[code[j]] -= 1
    else:
        print('n')
        sys.exit()
print('y')