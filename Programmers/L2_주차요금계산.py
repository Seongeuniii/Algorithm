import math

def caltime(a, b):
    A = list(map(int, a.split(':')))
    B = list(map(int, b.split(':')))
    return (B[0]*60+B[1]) - (A[0]*60+A[1])

def solution(fees, records):
    answer = []
    in_time = {}
    total_time = {}

    for record in records:
        a, b, c = record.split()
        if c == 'IN': 
            in_time[b] = a
        else:
            result = caltime(in_time[b], a)
            try: total_time[b] += result
            except: total_time[b] = result
            in_time[b] = 0

    for key, value in sorted(in_time.items()):
        if value != 0:
            result = caltime(value, '23:59')
            try: total_time[key] += result
            except: total_time[key] = result

        if total_time[key] <= fees[0]: 
            money = fees[1]
        else: 
            money = fees[1] + math.ceil((total_time[key] - fees[0]) / fees[2]) * fees[3]
        
        answer.append(money)
        
    return answer