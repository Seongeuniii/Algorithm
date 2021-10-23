from itertools import permutations
n = int(input())
k = int(input())
card = list(input() for _ in range(n))
result = set()
for A in list(permutations(card,k)):
  result.add(''.join(A))
print(len(result))