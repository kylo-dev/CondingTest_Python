def solution(a, b, n):
    # 받은 콜라
    answer = 0
    
    while n >= a:
        remain_bottle = n % a
        n = (n//a) * b
        answer += n
        
        n += remain_bottle
    return answer