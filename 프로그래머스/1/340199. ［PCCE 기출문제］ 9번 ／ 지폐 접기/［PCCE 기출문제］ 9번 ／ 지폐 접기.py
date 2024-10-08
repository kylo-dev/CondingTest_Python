def solution(wallet, bill):
    answer = 0
    
    while min(bill) > min(wallet) or max(bill) > max(wallet):
        idx = bill.index(max(bill))
        bill[idx] = int(bill[idx] / 2)
        answer += 1
    
    return answer