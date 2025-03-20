def solution(word):
    answer = 0
    words = []
    moum = "AEIOU"
    
    def dfs(cnt, w):
        if cnt == 5:
            return
        
        for i in range(len(moum)):
            word = w + moum[i]
            words.append(word)
            dfs(cnt + 1, word)
    
    dfs(0, "")
    
    return words.index(word) + 1