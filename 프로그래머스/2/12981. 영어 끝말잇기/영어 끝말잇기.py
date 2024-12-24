def solution(n, words):
    answer = []
    use_word = []
    
    for idx, word in enumerate(words):
        if idx == 0:
            use_word.append(word)
            continue    
        
        if word in use_word or use_word[-1][-1] != word[0]:
            person = (idx % n) + 1
            turn = (idx // n) + 1
            return [person, turn]
            
        use_word.append(word)

    return [0, 0]