from collections import deque

N, K = map(int, input().split())

ans_time, ans_count = -1, 0
MAX = 100001
visited = [-1] * MAX

def bfs(position):
    global ans_time, ans_count

    que = deque([(position, 0)])
    visited[position] = 0

    while que:
        current, time = que.popleft()

        if current == K:
            if ans_time == -1:
                ans_time = time
                ans_count = 1
            elif time == ans_time:
                ans_count += 1
            continue
        
        for move in (current + 1, current - 1, current * 2):
            if 0 <= move < MAX and (visited[move] == -1 or visited[move] == time + 1):
                visited[move] = time + 1
                que.append((move, time + 1))

bfs(N)

print(ans_time)
print(ans_count)