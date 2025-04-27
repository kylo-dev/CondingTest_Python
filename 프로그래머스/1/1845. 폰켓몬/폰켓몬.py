from collections import Counter

def solution(nums):
    
    choice = len(nums) // 2
    num_count = Counter(nums)
    
    answer = len(num_count) if len(num_count) < choice else choice
    
    return answer

    