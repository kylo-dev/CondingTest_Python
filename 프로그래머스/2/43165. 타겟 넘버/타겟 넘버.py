def solution(numbers, target):
    answer = 0
    N = len(numbers)
    
    def dfs(idx, total):
        nonlocal answer
        
        if idx == N and total == target:
            answer += 1
            return
        elif idx == N:
            return
        
        dfs(idx + 1, total + numbers[idx])
        dfs(idx + 1, total - numbers[idx])
    
    dfs(0, 0)
    
    return answer