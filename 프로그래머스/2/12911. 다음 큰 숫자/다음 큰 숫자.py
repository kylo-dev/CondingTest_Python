def solution(n):
    answer = n
    n_cnt = bin(n).count('1')
    
    while True:
        answer += 1
        if (bin(answer).count('1') == n_cnt):
            return answer
