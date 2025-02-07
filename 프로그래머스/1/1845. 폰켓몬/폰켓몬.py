def solution(nums):
    answer = 0
    
    cnt = len(nums) // 2
    n_set = set(nums)
    
    answer = cnt if cnt < len(n_set) else len(n_set)
    
    return answer