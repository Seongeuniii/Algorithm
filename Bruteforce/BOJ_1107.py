import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
if M:
  button = list(input().strip())
else:
  button = []

answer = abs(N-100)

def check(num):
  for n in str(num):
    if n in button:
      return 0
  return 1

for i in range(answer):
  test = N+i
  if check(test):
    answer = min(answer, abs(N-test)+len(str(test)))
  test = N-i
  if test >= 0 and check(test):
    answer = min(answer, abs(N-test)+len(str(test)))

print(answer)