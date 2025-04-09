def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2])
    island = [i for i in range(n)]
    
    def find(x):
        if island[x] != x:
            island[x] = find(island[x])
        return island[x]
    
    def union(a, b):
        root_a = find(a)
        root_b = find(b)
        
        if root_a != root_b:
            island[root_b] = root_a
            return True
        return False
    
    for start, end, cost in costs:
        if union(start, end):
            answer += cost
    
    return answer