import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = float('inf')

def sum_ability(team):
    total = 0
    
    for comb in combinations(team, 2):
        a, b = comb
        total += arr[a][b] + arr[b][a]
    return total

players = [i for i in range(N)]
for start_team in combinations(players, N // 2):
    
    if 0 not in start_team:
        continue

    link_team = [i for i in players if i not in start_team]
    diff = abs(sum_ability(start_team) - sum_ability(link_team))
    answer = min(answer, diff)

print(answer)