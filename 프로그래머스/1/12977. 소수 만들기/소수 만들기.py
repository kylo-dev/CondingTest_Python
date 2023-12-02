from itertools import combinations

def sosu(rel):
    for i in range(2, int(rel**0.5)+1):
        if rel % i == 0:
            flag = True
            break
        else:
            flag = False
    return flag

def solution(nums):
    answer = 0
    
    for i in list(combinations(nums, 3)):
        tol = sum(i)
        rel = sosu(tol)
        if not rel:
            answer +=1

    return answer
