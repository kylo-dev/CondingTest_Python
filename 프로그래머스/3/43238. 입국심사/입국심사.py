def solution(n, times):
    answer = 0
    
    left, right = min(times), max(times) * n
    
    while left <= right:
        mid = (left + right) // 2
        count = 0
        
        for time in times:
            count += mid // time
        
        if count < n:
            left = mid + 1
        
        if count >= n:
            right = mid - 1
            answer = mid
    
    return answer