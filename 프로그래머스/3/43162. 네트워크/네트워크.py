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
            for i in range(len(computers)):
                if not visited[i] and computers[computer][i]:
                    que.append(i)
                    visited[i] = True
    
    return answer