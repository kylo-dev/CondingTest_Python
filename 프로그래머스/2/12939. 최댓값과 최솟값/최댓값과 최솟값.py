def solution(s):
    answer = []
    nums = s.split(" ")
    nums = list(map(int, nums))
    
    answer.append(min(nums))
    answer.append(max(nums))
    
    return ' '.join(map(str, answer))