def dfs(numbers, target, idx, values):
    global answer
    
    if (idx == len(numbers) and values == target):
        answer += 1
        return
    elif idx == len(numbers):
        return
    
    dfs(numbers, target, idx+1, values + numbers[idx])
    dfs(numbers, target, idx+1, values - numbers[idx])
    

def solution(numbers, target):
    global answer
    answer = 0
    
    dfs(numbers, target, 0, 0)
    
    return answer
    