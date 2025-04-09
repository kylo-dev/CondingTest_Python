from collections import defaultdict

def solution(clothes):
    
    clothes_dict = defaultdict(list)
    
    for cloth_name, cloth_type in clothes:
        clothes_dict[cloth_type].append(cloth_name)
    
    answer = 1
    for cloth in clothes_dict:
        answer *= len(clothes_dict[cloth]) + 1
    
    return answer - 1