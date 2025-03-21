from collections import deque

def solution(n, computers):
    visited = [False] * n
    answer = 0
    
    for i in range(n):
        if not visited[i]:
            que = deque([i])
            visited[i] = True
            answer += 1
        while que:
            comp = que.popleft()
            for i in range(n):
                if not visited[i] and computers[comp][i] == 1:
                    que.append(i)
                    visited[i] = True
    
    return answer