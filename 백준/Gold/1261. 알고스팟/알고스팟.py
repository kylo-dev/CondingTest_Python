from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
INF = 10 ** 9

dist = [[INF] * M for _ in range(N)]
dist[0][0] = 0

que = deque([(0, 0)])

while que:
    x, y = que.popleft()

    if x == N - 1 and y == M - 1:
        print(dist[-1][-1])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            cost = dist[x][y] + arr[nx][ny]

            if cost < dist[nx][ny]:
                dist[nx][ny] = cost

                if arr[nx][ny] == 0:
                    que.appendleft((nx, ny))
                else:
                    que.append((nx, ny))