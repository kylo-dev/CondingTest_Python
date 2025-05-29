import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
all_team = set([i for i in range(N)])
answer = float('inf')

def sum_ability(team):
    sum = 0
    for comb in combinations(team, 2):
        a, b = comb
        sum += arr[a][b]
        sum += arr[b][a]
    return sum

for start_team in combinations(all_team, N // 2):
    link_team = all_team - set(start_team)

    start_sum = sum_ability(start_team)
    link_sum = sum_ability(link_team)

    answer = min(answer, abs(start_sum - link_sum))

print(answer)