from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    genre_dict = defaultdict(list)
    for i in range(len(genres)):
        genre_dict[genres[i]].append([plays[i], i])
    
    genre_rank = {}
    for genre in genre_dict:
        total = sum([i[0] for i in genre_dict[genre]])
        genre_rank[genre] = total
    
    genre_rank = sorted(genre_rank.items(), key = lambda x: -x[1])
    
    for i in range(len(genre_rank)):
        cnt = 0
        genre = genre_rank[i][0]
        
        rank_list = genre_dict[genre]
        rank_list.sort(key = lambda x : (-x[0], x[1]))
        
        for play, idx in genre_dict[genre]:
            if cnt == 2:
                break
            else:
                answer.append(idx)
                cnt += 1
    return answer