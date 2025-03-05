def solution(word):
    
    answer = 0
    words = []
    word5 = 'AEIOU'
    
    def dfs(cnt, w):
        if cnt == 5:
            return
        for i in range(len(word5)):
            wo = w + word5[i]
            words.append(wo)
            dfs(cnt + 1, wo)
    dfs(0, "")
    
    return words.index(word) + 1