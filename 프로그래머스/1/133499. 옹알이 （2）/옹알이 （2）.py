def solution(babbling):
    words = ["aya", "ye", "woo", "ma" ]
    answer = 0
    for bab in babbling:
        for w in words:
            if w * 2 not in bab:
                bab = bab.replace(w, " ")
        if bab.isspace():
            answer += 1
    return answer