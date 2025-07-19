from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre_sum_dict = defaultdict(int)
    genre_dict = defaultdict(list)
    
    # 장르별 총 플레이 수 집계
    for i in range(len(genres)):
        genre_sum_dict[genres[i]] += plays[i]
        genre_dict[genres[i]].append((i, plays[i]))  # 동시에 삽입

    # 총 플레이 수 기준으로 장르 정렬
    sorted_genre_sum = sorted(genre_sum_dict.items(), key=lambda x: -x[1])
    
    # 각 장르 내에서 곡을 (재생 수 내림차순, 고유 번호 오름차순)으로 정렬
    for genre in genre_dict:
        genre_dict[genre].sort(key=lambda x: (-x[1], x[0]))

    # 각 장르에서 최대 2개씩 추출
    for genre, _ in sorted_genre_sum:
        for i in range(min(2, len(genre_dict[genre]))):
            answer.append(genre_dict[genre][i][0])
    
    return answer