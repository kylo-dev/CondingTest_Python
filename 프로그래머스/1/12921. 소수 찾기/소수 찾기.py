def solution(n):
    answer = 0
    
    for i in range(2, n+1):
        flag = True
        
        for j in range(2, int(i**0.5)+1):
            if i == 2:
                flag = True
                break
            if i % j == 0:
                flag = False
                break
            else:
                flag = True
        if flag:
            answer += 1
    
    return answer