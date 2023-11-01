def solution(s):
    answer = []
    d = {}
    
    for i in s:
        if i not in d.keys():
            answer.append(-1)
            d[i] = s.index(i)
        elif i in d.keys():
            index = s.index(i, d[i]+1) - d[i]
            answer.append(index)
            d[i] = s.index(i,d[i]+1)
    return answer