from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    def bfs(start):
        q = deque([start])
        visited[start] = True

        while q:
            idx = q.popleft()

            for i in range(n):
                if computers[idx][i] == 1 and not visited[i]:
                    q.append(i)
                    visited[i] = True
    
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1

    return answer