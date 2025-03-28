def solution(distance, rocks, n):
    
    # 바위 간의 거리가 최소인 상황에서 최대 값을 구해야 한다.
    left = 1
    right = distance
    
    rocks.sort()
    rocks.append(distance)
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2
        del_rock = 0
        prev_rock = 0
        
        for rock in rocks:
            dist = rock - prev_rock
            
            if dist < mid:
                del_rock += 1
                # 허용 가능한 거리(mid)가 아니였음
                if del_rock > n:
                    break
            else:
                 prev_rock = rock   
                    
        if del_rock > n:
            right = mid - 1
        else:
            left = mid + 1
            answer = mid
    
    return answer
    