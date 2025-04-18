from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    tang_count = dict(Counter(tangerine))
    tang_count = sorted(tang_count.items(), key = lambda x: (-x[1]))
    
    for size, cnt in tang_count:
        k -= cnt
        answer += 1
        if k <= 0:
            break
    
    return answer