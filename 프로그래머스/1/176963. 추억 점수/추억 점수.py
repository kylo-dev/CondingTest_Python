def solution(name, yearning, photo):
    answer = []
    
    for p in photo:
        result = 0
        for n in p:
            if n in name:
                idx = name.index(n)
                result += yearning[idx]
        answer.append(result)
    return answer