import sys
input = sys.stdin.readline

def solution(phone_book):
  s = set()

  for num in phone_book:
    for i in range(1, len(num)):
      s.add(num[:i])

  if len(s) + len(phone_book) == len(s.union(set(phone_book))):
    print('YES')
  else:
    print('NO')


for _ in range(int(input())):
  N = int(input())
  solution(list(input().strip() for _ in range(N)))