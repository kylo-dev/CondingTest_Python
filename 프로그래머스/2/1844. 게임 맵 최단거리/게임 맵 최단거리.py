from collections import deque

def solution(maps):
    
    N = len(maps)
    M = len(maps[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[0] * M for _ in range(N)]
    
    que = deque([(0, 0)])
    visited[0][0] = 1
    
    while que:
        x, y = que.popleft()
        
        if x == M-1 and y == N-1:
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 1:
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    que.append((nx, ny))
    
    return visited[-1][-1] if visited[-1][-1] != 0 else -1