import math

def solution(n, stations, w):
    answer = 0
    prev_end = 1
    
    for station in stations:
        start = station - w
        end = station + w
        
        diff = start - prev_end
        answer += math.ceil(diff / (w * 2 + 1))
        prev_end = end + 1
    
    if prev_end <= n:
        diff = n - prev_end + 1
        answer += math.ceil(diff / (w * 2 + 1))
    
    return answer