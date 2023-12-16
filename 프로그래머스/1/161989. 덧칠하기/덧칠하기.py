def solution(n, m, section):
    answer = 0
    tmp = 0
    
    for i in section:
        if tmp <= i :
            tmp = i + m
            answer += 1    
    return answer