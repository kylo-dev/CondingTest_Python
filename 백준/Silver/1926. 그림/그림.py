import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = []
visited = [[False] * M for _ in range(N)]

def bfs(i, j):
    que = deque([(i, j)])
    cnt = 1
    visited[i][j] = True

    while que:
        x, y = que.popleft()
        arr[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if arr[nx][ny] == 1:
                    que.append((nx, ny))
                    visited[nx][ny] = True
                    cnt += 1
    return cnt

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            answer.append(bfs(i, j))

if answer:
    print(len(answer))
    print(max(answer))
else:
    print(0)
    print(0)