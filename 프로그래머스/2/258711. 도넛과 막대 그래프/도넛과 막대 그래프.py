def solution(edges):
    
    # 도넛 (n : n)
    # 막대 (n : n-1)
    # 8자 모양 (2n+1 : 2n+2)
    
    answer = []
    edge_dict = {}
    max_val = 0
    
    for edge in edges:
        if max_val < max(edge):
            max_val = max(edge)
        if edge[1] not in edge_dict:
            edge_dict[edge[1]] = []
        if edge[0] not in edge_dict:
            edge_dict[edge[0]] = [edge[1]]
        else:
            edge_dict[edge[0]].append(edge[1])
    
    # 방문처리
    visited = [0 for _ in range(max_val + 1)]
    
    # 생성한 정점 찾기 : 도착 지점 노드 제거 & 간선 개수 1개 제거
    for i in edge_dict.values():
        for j in i:
            visited[j] = 1
    for i in edge_dict.keys():
        if len(edge_dict[i]) <= 1:
            visited[i] = 1
    
    for idx, val in enumerate(visited):
        if idx != 0 and val == 0:
            created_node = idx
    
    result = [0 for _ in range(4)]
    visited = [0 for _ in range(max_val + 1)]
    
    def dfs(val):
        start = val
        visited[start] = 1
        stack = [val]
        
        while stack:
            cur = stack.pop()
            
            # 막대 모양 : 끝이 존재
            if len(edge_dict[cur]) == 0:
                result[2] += 1
                return
            if len(edge_dict[cur]) == 1:
                if visited[edge_dict[cur][0]] == 0:
                    stack.append(edge_dict[cur][0])
                else:
                    result[1] += 1
                    return
            if len(edge_dict[cur]) == 2:
                result[3] += 1
                return
    
    result[0] = created_node
    for i in edge_dict[created_node]:
        dfs(i)
    
    return result
                    
    
            