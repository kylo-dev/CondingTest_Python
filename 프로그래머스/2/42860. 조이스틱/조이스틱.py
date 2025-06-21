def solution(name):
    answer = 0
    
    N = len(name)
    for ch in name:
        answer += min([ord(ch) - ord('A'), ord('Z') - ord(ch) + 1])
    
    move = N - 1
    for i in range(N):
        next_i = i + 1
        
        while next_i < N and name[next_i] == 'A':
            next_i += 1
        
        # move - left - right
        move = min([move, i + i + (N - next_i), i + (N - next_i) * 2])
        
    return answer + move