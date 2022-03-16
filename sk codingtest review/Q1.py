# 문제 설명
# 6종류(1원, 5원, 10원, 50원, 100원, 500원)의 동전을 생산하는 공장이 있다.
# 각 동전의 생산 단가가 주어지고 특정 금액만큼 동전을 생산해달라는 의뢰가 들어왔을 때, 그 금액만큼 동전을 생샌하는 최소비용을 구해야한다.

# 입력
# 공장이 생산해야 하는 금액을 나타내는 정수 money, 
# 6종류 동전의 생산 단가를 나타내는 1차원 정수 배열 costs가 매개변수로 주어집니다. 
# money원만큼의 동전을 최소 비용으로 생산했을 때, 그 최소 비용을 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ money ≤ 1,000,000
# costs의 길이 = 6
# 1 ≤ costs의 원소 ≤ 5,000

# 입출력 예시

# 입력
# 4578	[1, 4, 99, 35, 50, 1000]	
# 출력
# 2308

# 입력
# 1999	[2, 11, 20, 100, 200, 600]
# 출력	
# 2798

import math

def solution(money, costs):
    value = [1, 5, 10, 50, 100, 500]
    
    dp = [math.inf]*(money + 1)
    dp[0] = 0

    for i in range(1, money + 1):
        for j, cost in enumerate(costs):
            if value[j] > i:
                continue
            dp[i] = min(dp[i], dp[i - value[j]] + cost)

    return dp[-1]