def solution():
  global K
  section = []

  for i in range(1, len(sensor)):
    section.append(sensor[i]-sensor[i-1])

  section.sort()

  while section and K > 1:
    # 가장 긴 구간 삭제
    section.pop()
    K -= 1

  return sum(section)

N = int(input())
K = int(input())
sensor = sorted(list(set(map(int,input().split()))))

print(solution())