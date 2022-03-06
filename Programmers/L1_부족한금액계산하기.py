# 2분

def solution(price, money, count):
    m = (count * (count + 1) // 2) * price

    if money >= m:
        return 0
    else:
        return m-money