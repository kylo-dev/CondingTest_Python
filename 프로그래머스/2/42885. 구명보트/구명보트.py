def solution(people, limit):
    answer = 0
    
    people.sort()
    start, end = 0, len(people) - 1
    
    while start <= end:
        total = people[start] + people[end]
        
        if total > limit:
            end -= 1
            answer += 1
        else:
            start += 1
            end -= 1
            answer += 1
    
    return answer