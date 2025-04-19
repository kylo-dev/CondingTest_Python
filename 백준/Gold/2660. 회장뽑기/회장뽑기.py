from collections import deque

n = int(input())
arr = [list() for _ in range(n + 1)]

while True:
    u, v = map(int, input().split())

    if u == -1 and v == -1:
        break
    arr[u].append(v)
    arr[v].append(u)

def bfs(pos):
    visited = [-1] * (n + 1)
    visited[pos] = 0

    que = deque([pos])

    while que:
        cur = que.popleft()

        for next_pos in arr[cur]:
            if visited[next_pos] == -1:
                visited[next_pos] = visited[cur] + 1
                que.append(next_pos)
    
    return max(visited)

candidate_score = 0
score = 50

for i in range(1, n + 1):
    candidate_score = bfs(i)

    if candidate_score < score:
        candidates = [i]
        score = candidate_score
    elif candidate_score == score:
        candidates.append(i)

print(score, len(candidates))
print(' '.join(map(str, sorted(candidates))))