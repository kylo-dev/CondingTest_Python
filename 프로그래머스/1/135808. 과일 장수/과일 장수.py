def solution(k, m, score):
    answer = 0
    arr = []
    score.sort(reverse=True)
    
    for i in range(len(score)//m):
        arr.append(score[i*m : m*(1+i)])
    
    for j in arr:
        answer += min(j) * m
    return answer
    
    # idx = 0
    # while len(score) >= m:
    #     for i in range(m):
    #         arr[idx].append(max(score))
    #         score.remove(max(score))
    #     idx += 1
