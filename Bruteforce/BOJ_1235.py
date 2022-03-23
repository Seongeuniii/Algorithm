import sys
input = sys.stdin.readline

N = int(input())
students = [input().strip() for _ in range(N)]
l = len(students[0])

for k in range(1, l+1):
  s = set()
  for std in students:
    s.add(std[l-k:])
  if len(s) == N:
    print(k)
    break