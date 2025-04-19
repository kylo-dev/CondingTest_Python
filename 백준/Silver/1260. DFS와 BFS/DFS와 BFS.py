from collections import deque

N, M, V = map(int, input().split())

arr = [list() for _ in range(N + 1)]

bfs_ans = []
dfs_ans = []

b_visited = [False for _ in range(N + 1)]
d_visited = [False for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())

    arr[u].append(v)
    arr[v].append(u)

for i in range(1, len(arr)):
    arr[i].sort()

def dfs(n):
    
    d_visited[n] = True
    dfs_ans.append(n)

    for next_pos in arr[n]:
        if not d_visited[next_pos]:
            dfs(next_pos)

dfs(V)
print(' '.join(map(str, dfs_ans)))

def bfs(n):
    que = deque([n])
    b_visited[n] = True

    while que:
        pos = que.popleft()
        bfs_ans.append(pos)

        for next_pos in arr[pos]:
            if not b_visited[next_pos]:
                b_visited[next_pos] = True
                que.append(next_pos)

bfs(V)
print(' '.join(map(str, bfs_ans)))