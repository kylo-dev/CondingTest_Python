from itertools import combinations
import sys
input = sys.stdin.readline


while True:
    case = list(map(int, input().split()))
    ans = []
    if case == [0]:
        break

    k = case[0]
    arr = sorted(case[1:])

    for i in combinations(arr, 6):
        ans.append(i)
    
    ans.sort()
    for a in ans:
        print(' '.join(map(str, a)))
        
    print()
