def solution(genres, plays):
    answer = []
    total = {} # {'장르': '총 재생 횟수'}
    gen = {} # {'장르': [(재생 횟수, 고유번호)]}
    
    for i in range(len(genres)):
        total[genres[i]] = total.get(genres[i], 0) + plays[i]
        if genres[i] not in gen:
            gen[genres[i]] = [(plays[i], i)]
        else:
            gen[genres[i]].append((plays[i], i))
            
    total = sorted(total.items(), key = lambda x: -x[1])
    # gen = sorted(gen.values(), key = lambda x: (-x[0], x[1]))
    
    for genre, play in total:
        cnt = 0
        result = sorted(gen[genre], key = lambda x: (-x[0], x[1]))
        for i in range(len(result)):
            if cnt == 2:
                break
            answer.append(result[i][1])
            cnt += 1
    
    return answer