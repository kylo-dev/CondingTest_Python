def solution(lottos, win_nums):
    answer = []
    
    grade_dict = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    zero_count = lottos.count(0)
    max_grade = 0
    min_grade = 0
    
    for lotto in lottos:
        if lotto in win_nums:
            min_grade += 1
    
    max_grade = min_grade + zero_count
    answer.append(grade_dict.get(max_grade))
    answer.append(grade_dict.get(min_grade))
    
    return answer