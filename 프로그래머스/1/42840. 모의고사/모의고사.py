def solution(answers):
    answer = [0, 0, 0]
    result = []
    
    std1 = [1, 2, 3, 4, 5]
    std2 = [2, 1, 2, 3, 2, 4, 2, 5]
    std3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i in range(len(answers)):
        ans = answers[i]
        
        if std1[i % len(std1)] == ans:
            answer[0] += 1
        if std2[i % len(std2)] == ans:
            answer[1] += 1
        if std3[i % len(std3)] == ans:
            answer[2] += 1
    
    max_score = max(answer)
    for i in range(len(answer)):
        if answer[i] == max_score:
            result.append(i + 1)
    
    return result