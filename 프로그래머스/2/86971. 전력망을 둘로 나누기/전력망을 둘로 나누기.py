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
        answer = min(diff, answer)
    
    return answer    
    
def bfs(start, visited, graph):
    que = deque([start])
    visited[start] = True
    cnt = 1
    
    while que:
        st = que.popleft()
        
        for point in graph[st]:
            if not visited[point]:
                cnt += 1
                visited[point] = True
                que.append(point)
    
    return cnt
    
    