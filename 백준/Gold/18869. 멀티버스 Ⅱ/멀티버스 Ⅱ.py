import sys
input = sys.stdin.readline
from collections import Counter
from bisect import bisect_left


N, M = map(int, input().split())
spaces = [
    list(map(int, input().split()))
    for _ in range(N)
]
sorted_spaces = []

# 우주 정렬하여, idx 설정
for space in spaces:
    rank = {num: i for i, num in enumerate(sorted(space))}
    idx_list = [rank[num] for num in space]
    
    sorted_spaces.append(tuple(idx_list))

# dict 카운트
space_count = Counter(sorted_spaces)

answer = 0
for sp_cnt in space_count.values():
    answer += (sp_cnt * (sp_cnt - 1)) // 2

print(answer)