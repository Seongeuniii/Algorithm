def solution(answers):
    answer = []
    
    students = [
            [1, 2, 3, 4, 5], 
            [2, 1, 2, 3, 2, 4, 2, 5], 
            [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
          ]
    score = [0]*len(students)
    
    for i, ans in enumerate(answers):
        for j, std in enumerate(students):
            if ans == std[i % len(std)]:
                score[j] += 1
                
    S = max(score)
    for i, s in enumerate(score):
        if s == S:
            answer.append(i+1)
            
    return answer