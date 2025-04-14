import sys
input = sys.stdin.readline
from collections import deque

# (1,1) -> (n, m)
# 벽 1개까지 부실 수 있음

N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]

def bfs():
    que = deque([(0, 0, 0, 1)])
    visited[0][0][0] = True

    while que:
        x, y, is_delete, dist = que.popleft()
        if x == N - 1 and y == M-1:
            return dist

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == '0' and not visited[nx][ny][is_delete]:
                    visited[nx][ny][is_delete] = True
                    que.append((nx, ny, is_delete, dist + 1))
                elif arr[nx][ny] == '1' and not is_delete and not visited[nx][ny][1]:
                    visited[nx][ny][1] = True
                    que.append((nx, ny, 1, dist + 1))
    return -1

print(bfs())
