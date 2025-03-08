from collections import deque

def solution(begin, target, words):
    answer = 0
    
    visited = [False] * len(words)
    que = deque([(begin, 0)])
    
    while que:
        word ,cnt = que.popleft()
        if word == target:
                return cnt
        
        for i in range(len(words)):
            if check(word, words[i]) and not visited[i]:
                visited[i] = True
                que.append((words[i], cnt + 1))
    return 0

def check(w1, w2):
    diff = sum(1 for a, b in zip(w1, w2) if a != b)
    return diff == 1