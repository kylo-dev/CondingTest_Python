def solution(clothes):
    clo_dict = {}
    
    for clo, ty in clothes:
        if ty not in clo_dict:
            clo_dict[ty] = 1
        else:
            clo_dict[ty] += 1
    
    answer = clo_dict.values()
    total = 1
    for t in answer:
        total *= (t+1)
    return total - 1