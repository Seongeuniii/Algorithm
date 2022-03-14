# 2839
def solution():

  for i in range(N//5, -1, -1):
    if (N - (5*i)) % 3 == 0:
      return i + (N - (5*i)) // 3

  return -1

N = int(input())
print(solution())



# 1931
def solution():
  answer = 0
  end = 0

  for s, e in meetings:
    if s >= end:
      answer += 1 
      end = e

  return answer

N = int(input())
meetings = [list(map(int,input().split())) for _ in range(N)]
meetings.sort(key = lambda  x:(x[1], x[0]))

print(solution())



# 11047
def solution():
  global K
  answer = 0

  for v in reversed(value):
    answer += K // v
    K %= v

  return answer

N, K = map(int, input().split())
value = [int(input()) for _ in range(N)]

print(solution())



# 2839
def solution():
  answer = 0

  A.sort()
  B.sort(reverse=True)

  for i in range(N):
    answer += A[i]*B[i]

  return answer

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

print(solution())



# 1541
def solution():
  answer = []

  for s in S:
    answer.append(sum(list(map(int,s.split('+')))))

  return answer[0] - sum(answer[1:])

S = input().strip().split('-')

print(solution())



# 5585
def solution():
  change = 1000-N
  answer = 0

  coin = [500, 100, 50, 10, 5, 1]

  for c in coin:
    answer += change // c
    change %= c

  return answer

N = int(input())
print(solution())