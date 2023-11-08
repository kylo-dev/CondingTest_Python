def solution(k, score):
    answer = []
    arr = []
    for i in score:
        if (len(arr) < k):
            arr.append(i)
            answer.append(min(arr))
        else:
            if i > min(arr):
                arr.pop(arr.index(min(arr)))
                arr.append(i)
                answer.append(min(arr))
            else:
                answer.append(min(arr))
    
    return answer