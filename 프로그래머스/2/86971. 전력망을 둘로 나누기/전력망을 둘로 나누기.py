from collections import deque

def solution(n, wires):
    answer = n
    
    graph = [[] for _ in range(n + 1)]
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    for start, end in wires:
        visited = [False for _ in range(n + 1)]
        visited[end] = True
        cnt = bfs(start, visited, graph)
        
        diff = abs(cnt - (n - cnt))
        answer = min(answer, diff)
    
    return answer
    
def bfs(start, visited, graph):
    cnt = 1
    que = deque([start])
    visited[start] = True
    
    while que:
        point = que.popleft()
        
        for i in graph[point]:
            if not visited[i]:
                cnt += 1
                visited[i] = True
                que.append(i)
    return cnt
    