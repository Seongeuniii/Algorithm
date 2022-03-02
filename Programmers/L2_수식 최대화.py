from itertools import permutations

def solution(expression):
    answer = 0
    
    op = ['+', '-', '*']
    numList = []
    opList = []
    
    num = ''
    for e in expression:
        if e in op:
            opList.append(e)
            numList.append(num)
            num = ''
        else:
            num += e
    numList.append(num)
    
    cases = list(permutations(op, 3))
    for case in cases:
        na = numList
        oa = opList
        
        for setop in case:
            nb = [na[0]]
            ob = []
            
            for i in range(len(oa)):
                if oa[i] == setop:
                    a = nb.pop()
                    nb.append(str(eval(a + oa[i] + na[i+1])))
                else:
                    nb.append(na[i+1])
                    ob.append(oa[i])
            
            na = nb
            oa = ob
            
        answer = max(answer, abs(int(na[0])))
    
    return answer