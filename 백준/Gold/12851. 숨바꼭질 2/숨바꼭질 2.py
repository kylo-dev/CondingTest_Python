from collections import deque

min_time, count = -1, 0
MAX = 100001

visited = [-1] * MAX

N, K = map(int, input().split())

def bfs(position):
    global min_time, count

    que = deque([(position, 0)])
    visited[position] = 0

    while que:
        cur, time = que.popleft()

        if cur == K:
            if min_time == -1:
                count = 1
                min_time = time
            elif time == min_time:
                count += 1
        
        for move in (cur + 1, cur - 1, cur * 2):
            if 0 <= move < MAX:
                if visited[move] == -1 or visited[move] == time + 1:
                    que.append((move, time + 1))
                    visited[move] = time + 1

bfs(N)

print(min_time)
print(count)