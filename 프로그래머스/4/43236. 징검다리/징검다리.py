def solution(distance, rocks, n):
    left = 1
    right = distance
    
    rocks.sort()
    rocks.append(distance)
    
    while left <= right:
        mid = (left + right) // 2
        delete_rock = 0
        prev_rock = 0
        
        for rock in rocks:
            dist = rock - prev_rock
            if dist < mid:
                delete_rock += 1
                
                if delete_rock > n:
                    break
            else:
                prev_rock = rock
        
        # 커트라인이 큰 경우
        if delete_rock > n:
            right = mid - 1
        else:
            left = mid + 1
            answer = mid
    
    return answer