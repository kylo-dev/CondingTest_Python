from collections import deque

def solution(n, m, x, y, r, c, k):
    
    def get_diff(x1, y1):
        return abs(x1 - (r-1)) + abs(y1 - (c-1))
    
    if get_diff(x-1, y-1) > k or (get_diff(x-1, y-1) - k) % 2:
        return "impossible"
    
    # 탐색 방향 사전 순
    direct = {(1, 0): "d", (0, -1): "l", (0, 1): "r", (-1, 0): "u"}
    
    que = deque([(x-1, y-1, 0, "")])
    
    while que:
        i, j, cnt, route = que.popleft()
        
        if (i, j) == (r-1, c-1) and (k-cnt) % 2:
            return "impossible"
        elif (i, j) == (r-1, c-1) and cnt == k:
            return route
        
        for dx, dy in direct:
            nx = i + dx
            ny = j + dy
            
            if 0 <= nx < n and 0 <= ny < m:
                if get_diff(nx, ny) + cnt + 1 > k:
                    continue
                que.append((nx, ny, cnt + 1, route+direct[(dx, dy)]))
                break