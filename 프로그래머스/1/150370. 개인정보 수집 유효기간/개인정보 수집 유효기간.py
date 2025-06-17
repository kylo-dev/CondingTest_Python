def check_privacy_term(today, privacy, term):
    today = tuple(map(int, today.split(".")))
    year, month, day = map(int, privacy.split("."))
    
    month += term
    day -= 1
    
    if day == 0:
        day = 28
        month -= 1
    
    year += (month - 1) // 12
    month = (month - 1) % 12 + 1

    privacy = (year, month, day)
    return today > privacy
    

def solution(today, terms, privacies):
    
    term_dict = {}
    answer = []
    
    for term in terms:
        term_type, period = term.split(" ")
        term_dict[term_type] = int(period)
    
    for idx, privacy in enumerate(privacies, start = 1):
        privacy_time, privacy_type = privacy.split(" ")
        if check_privacy_term(today, privacy_time, term_dict[privacy_type]):
            answer.append(idx)
        
    answer.sort()
    return answer