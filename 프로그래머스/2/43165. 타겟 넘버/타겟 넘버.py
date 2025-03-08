def solution(numbers, target):
    answer = 0
    
    leaves = [0]
    
    for num in numbers:
        temp = []
        
        for l in leaves:
            temp.append(l + num)
            temp.append(l - num)
        
        leaves = temp
    return leaves.count(target)
        
    
    return answer