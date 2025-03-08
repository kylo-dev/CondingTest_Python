def solution(numbers, target):
    
    def dfs(idx, total):
        if idx == len(numbers):
            return 1 if total == target else 0
        return dfs(idx+1, total + numbers[idx]) + dfs(idx+1, total - numbers[idx])
    
    return dfs(0, 0)