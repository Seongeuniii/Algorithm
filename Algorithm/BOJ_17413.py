import sys
S = sys.stdin.readline().strip()
result = ''
test = ''
cmd = False
for s in S:
    if cmd==False:
        if s == "<":
            result+=test[::-1]
            test=''
            cmd=True
            result+=s
        elif s == " ":
            result+=test[::-1]+' '
            test=''
        else:
            test+=s
    else:
        result+=s
        if s==">":
            cmd=False
print(result+test[::-1])