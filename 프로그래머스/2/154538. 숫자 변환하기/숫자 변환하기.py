from collections import deque

def solution(x, y, n):
    visited = set()
    que = deque([(x, 0)])
    
    while que:
        cur, cnt = que.popleft()
        if cur == y:
            return cnt
        
        for next_val in (cur + n, cur * 2, cur * 3):
            if next_val <= y and next_val not in visited:
                que.append((next_val, cnt + 1))
                visited.add(next_val)
    
    return -1