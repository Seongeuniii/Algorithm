# n개의 버튼이 일렬로 배열
# 1~m 사이의 정수 k개

def solution(n, m, k, records):
  # 좌표 압축을 통한 가장 작은 비밀번호 구하기
  t = list(set(records[0]))
  t.sort()
  dic_key = {t[i]: i+1 for i in range(len(t))} # 인덱싱
  min_key = list(map(lambda x: dic_key[x], records[0])) # 좌표 압축 결과
  
  # 최대한 벌려주자
  # possible[i]: 앞 숫자와 최대한 벌릴 수 있는 거리
  possible = [0] + [m-len(t)] * len(t)
  print('------testcase------')
  MAX = m-len(t)
  print('possible:', possible)

  # loop <= 1000
  for record in records:
    # 각 레코드에서 나오는 키 값을 중복 제거하고 정렬
    print('record:', record)
    keys = list(set(record))
    keys.sort()
    print('keys:', keys)
    # loop <= 5000
    for i in range(len(keys)):
      # 각 키 사이에 있는 숫자의 갯수
      if i == 0: 
        possible[i+1] = min(possible[i+1], keys[i]-1)
      else: 
        possible[i+1] = min(possible[i+1], keys[i]-keys[i-1]-1)
      print(i, possible)

  # 최대한 벌릴수 있는 값 이전까지 앞에서 벌려준 값을 포함해야 한다. 
  for i in range(len(t)):
    possible[i+1] = min(possible[i] + possible[i+1], MAX)

  print('final_possible:', possible)
  print('min_key:', min_key)
  max_key = list(map(lambda x: x+possible[x], min_key))

  return max_key

print(solution(8,	4,	4,	[[1, 5, 1, 3], [5, 7, 5, 6]]) == [1,3,1,2])
print(solution(8,	4,	4,	[[1, 8, 1, 3]]) == [1,4,1,3])
print(solution(10,	3,	3,	[[1, 2, 3], [5, 7, 10]]) == [1,2,3])
print(solution(10,	5,	3,	[[5, 7, 10]]) == [3,4,5])