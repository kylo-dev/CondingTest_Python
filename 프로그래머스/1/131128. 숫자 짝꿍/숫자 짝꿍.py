def solution(X, Y):
    answer = ''
    x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    for i in X:
        x[int(i)] += 1
    for j in Y:
        y[int(j)] += 1
    
    for i in range(9, -1, -1):
        value = str(i) * min(x[i], y[i])
        answer += value
    
    if len(answer) == 0:
        answer = "-1"
    if answer[0] == "0":
        answer = "0"
    return answer