def solution(word):
    
    alpha_moum = "AEIOU"
    moum = []
    
    def dfs(word):
        if len(word) == 5:
            return
        
        for i in range(len(alpha_moum)):
            temp_word = word + alpha_moum[i]
            moum.append(temp_word)
            dfs(temp_word)
    dfs('')
    
    return moum.index(word) + 1