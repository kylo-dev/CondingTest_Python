from collections import Counter

def solution(participant, completion):
    
    parti_count = Counter(participant)
    comp_count = Counter(completion)
    
    for key in parti_count:
        if key in comp_count and parti_count[key] != comp_count[key]:
            return key
        
        if key not in comp_count:
            return key