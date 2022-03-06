def solution(word):
    alphabet = ['', 'A', 'E', 'I', 'O', 'U']
    dic = set()

    for a in alphabet:
        for b in alphabet:
            for c in alphabet:
                for d in alphabet:
                    for e in alphabet:
                        dic.add(a+b+c+d+e)
    dic = sorted(list(dic))
    
    for i in range(len(dic)):
        if dic[i] == word:
            return i