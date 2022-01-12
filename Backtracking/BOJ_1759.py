#1
from itertools import combinations
L,C = map(int,input().split())
code = combinations(sorted(list(input().strip().split())),L)
vowel = ['a','e','i','o','u']

for cd in code:
  v_cnt, c_cnt = 0, 0
  for c in cd:
    if c in vowel: v_cnt += 1
    else: c_cnt += 1
  if v_cnt>=1 and c_cnt>=2:
    print(''.join(cd))

#2 
L,C = map(int,input().split())
code = sorted(list(input().strip().split()))

vowel = ['a','e','i','o','u']
answer = [('',0,0)]

for cd in code:
  test = []
  cnt = [1,0] if cd in vowel else [0,1]
  for a,b,c in answer:
    if len(a) > L: 
      continue
    test.append((a+cd, b+cnt[0], c+cnt[1]))
  answer += test

for e,f,g in sorted(answer, key=lambda x:(x[0], x[1], x[2])):
  if len(e)==L and f>=1 and g>=2:
    print(e)