import sys
input = sys.stdin.readline
from collections import deque

N, L, R = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0

def bfs(i, j, visited):
    que = deque([(i, j)])
    union = [(i, j)]
    visited[i][j] = True
    total = arr[i][j]

    while que:
        x, y = que.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(arr[x][y] - arr[nx][ny]) <= R:
                    total += arr[nx][ny]
                    union.append((nx, ny))
                    que.append((nx, ny))
                    visited[nx][ny] = True
    
    if len(union) == 1:
        return False
    
    avg = total // len(union)
    for x, y in union:
        arr[x][y] = avg
    
    return True

    
while True:
    visited = [[False for _ in range(N)] for _ in range(N)]
    moved = False

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and bfs(i, j, visited):
                moved = True
    
    if moved:
        answer += 1
    else:
        print(answer)
        break
            