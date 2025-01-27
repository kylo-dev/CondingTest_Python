from collections import deque

def solution(begin, target, words):
    answer = 0
    visited = [False] * len(words)
    q = deque([(begin, 0)])
    
    while q:
        word, depth = q.popleft()
        
        if word == target:
            return depth
        
        for i in range(len(words)):
            if check_word(word, words[i]) and not visited[i]:
                visited[i] = True
                q.append((words[i], depth + 1))
                
    return 0

def check_word(a, b):
    diff = sum(1 for x, y in zip(a, b) if x != y)
    return diff == 1