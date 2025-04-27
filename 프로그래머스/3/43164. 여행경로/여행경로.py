from collections import defaultdict

def solution(tickets):
    answer = []
    
    # a -> b
    ticket_dict = defaultdict(list)    
    for a, b in tickets:
        ticket_dict[a].append(b)
    
    for key in ticket_dict:
        ticket_dict[key].sort()
    
    def dfs(ticket):
        
        while ticket_dict[ticket]:
            dfs(ticket_dict[ticket].pop(0))
        
        answer.append(ticket)
    
    dfs("ICN")
    return answer[::-1]
    
    