import sys
from collections import Counter
from string import ascii_lowercase
alphabet_list = list(ascii_lowercase)
S = sys.stdin.readline().strip()
dic = Counter(S)
for l in alphabet_list:
  if l in dic:
    print(dic[l],end=' ')
  else:
    print(0,end=' ')