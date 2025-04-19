from collections import deque

n = int(input())
m = int(input())

arr = [list() for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

visited = [False for _ in range(n + 1)]

def bfs(n):
    que = deque([(n, 0)])
    visited[n] = True
    ans = 0

    while que:
        pos, cnt = que.popleft()

        if cnt > 2:
            continue

        for next_pos in arr[pos]:
            if not visited[next_pos] and cnt < 2:
                visited[next_pos] = True
                ans += 1
                que.append((next_pos, cnt + 1))
    
    return ans

print(bfs(1))
        