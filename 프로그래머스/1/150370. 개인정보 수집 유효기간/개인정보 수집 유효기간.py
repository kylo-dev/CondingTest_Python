def make_dday(date, term_mon):
    
    year, month, day = map(int, date.split("."))
    if month + term_mon > 12:
        new_year = year + (month + term_mon - 1) // 12
        new_month = (month + term_mon - 1) % 12 + 1
        if day == 1:
            new_day = 28
            new_month -= 1
        else:
            new_day = day - 1
    else:
        new_year = year
        new_month = month + term_mon
        if day == 1:
            new_day = 28
            new_month -= 1
        else:
            new_day = day - 1
    return (new_year, new_month, new_day)
        

def solution(today, terms, privacies):
    
    result = []
    
    term_dict = {}
    for term in terms:
        key, value = term.split()
        term_dict[key] = int(value)
    
    for privacy in privacies:
        date, term = privacy.split()
        term_mon = term_dict[term]
        
        result.append(make_dday(date, term_mon))
    
    answer = []
    today = tuple(map(int, today.split(".")))
    for i in range(len(result)):
        if result[i] < today:
            answer.append(i+1)
    
    return answer
    