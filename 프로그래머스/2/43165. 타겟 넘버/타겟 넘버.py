def solution(numbers, target):
    answer = 0
    
    def dfs(idx, values):
        nonlocal answer
        
        if idx == len(numbers) and values == target:
            answer += 1
            return
        elif idx == len(numbers):
            return
        
        dfs(idx + 1, values + numbers[idx])
        dfs(idx + 1, values - numbers[idx])
    
    dfs(0, 0)
    
    return answer