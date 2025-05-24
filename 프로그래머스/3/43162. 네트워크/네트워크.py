from collections import deque

def solution(n, computers):
    answer = 0
    
    visited = [False for _ in range(n)]
    
    for i in range(n):
        if not visited[i]:
            que = deque([i])
            visited[i] = True
            answer += 1
        
        while que:
            computer = que.popleft()
            for j in range(n):
                if not visited[j] and computers[computer][j] == 1:
                    visited[j] = True
                    que.append(j)
    
    return answer
                