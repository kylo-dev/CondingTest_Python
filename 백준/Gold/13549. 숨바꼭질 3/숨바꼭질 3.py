from collections import deque

N, K = map(int, input().split())
MAX = 100001

# 0초 후 2 * X -> X - 1, X + 1

visited = [False] * MAX

def bfs(n):
    que = deque([(n, 0)])
    visited[n] = True

    while que:
        cur, time = que.popleft()

        if cur == K:
            return time
        
        # 순간 이동
        next_cur = cur * 2
        if 0 <= next_cur < MAX and not visited[next_cur]:
            visited[next_cur] = True
            que.append((next_cur, time))

        for move in (cur - 1, cur + 1):
            if 0 <= move < MAX and not visited[move]:
                visited[move] = True
                que.append((move, time + 1))
    

print(bfs(N))