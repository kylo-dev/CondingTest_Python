def solution(word):
    
    word_list = ['A', 'E', 'I', 'O', 'U']
    words = []
    
    def dfs(w, cnt):
        if cnt == 5:
            return
        
        for i in range(5):
            wo = w + word_list[i]
            words.append(wo)
            dfs(wo, cnt+1)
    
    dfs('', 0)
    
    return words.index(word) + 1