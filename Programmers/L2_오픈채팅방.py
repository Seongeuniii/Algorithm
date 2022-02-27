def solution(records):
    answer = []
    printer = ['님이 나갔습니다.', '님이 들어왔습니다.']    
    
    kakao = []
    user = {}
    
    for record in records:
        record = record.split()
        
        if record[0] == 'Enter':
            kakao.append((1, record[1]))
            user[record[1]] = record[2]
        elif record[0] == 'Leave':
            kakao.append((0, record[1]))
        else:
            user[record[1]] = record[2]
        
    for a, b in kakao:
        answer.append(str(user[b]) + printer[a])
            
    return answer