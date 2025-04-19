import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
visited = [False for _ in range(N + 1)]

arr = [list() for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())

    arr[u].append(v)
    arr[v].append(u)

def bfs(n):
    que = deque([n])
    visited[n] = True

    while que:
        pos = que.popleft()

        for next_pos in arr[pos]:
            if not visited[next_pos]:
                que.append(next_pos)
                visited[next_pos] = True

ans = 0
for i in range(1, N + 1):
    if not visited[i]:
        bfs(i)
        ans += 1

print(ans)