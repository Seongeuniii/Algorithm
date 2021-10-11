import sys
name = sys.stdin.readline().strip()
dic = {}
for i in range(len(name)):
    try:
        dic[name[i]]+=1
    except:
        dic[name[i]] = 1
li = list(zip(dic.keys(),dic.values()))
li.sort(key = lambda x: x[0])
result = ''
odd = ''
for a,b in li:
    result+=a*(b//2)
    if b%2 != 0:
        if len(odd)==0:
            odd=a
        else:
            print("I'm Sorry Hansoo")
            sys.exit()
result = result+odd+result[::-1]
print(result)

# Counter클래스 사용
import sys
from collections import Counter
name = sys.stdin.readline().strip()
result = ''
odd = ''
for a,b in sorted(Counter(name).items()):
    result+=a*(b//2)
    if b%2 != 0:
        if len(odd)==0:
            odd=a
        else:
            print("I'm Sorry Hansoo")
            sys.exit()
result = result+odd+result[::-1]
print(result)