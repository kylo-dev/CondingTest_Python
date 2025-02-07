from collections import Counter

def solution(participant, completion):
    
    part = Counter(participant)
    
    for name in completion:
        part[name] -= 1
    
    for name, cnt in part.items():
        if cnt > 0:
            return name