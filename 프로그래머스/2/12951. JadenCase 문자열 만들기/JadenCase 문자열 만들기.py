def solution(s):
    s_list = s.split(" ")
    answer = []
    
    for s in s_list:        
        answer.append(s.capitalize())
    
    return " ".join(answer)