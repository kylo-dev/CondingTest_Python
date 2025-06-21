import sys
from itertools import permutations

N = int(input())
arr = list(map(int, input().split()))
operations = list(map(int, input().split()))

max_result = -float('inf')
min_result = float('inf')

def back(idx, total, ops):
    global max_result, min_result

    if idx == N:
        max_result = max(max_result, total)
        min_result = min(min_result, total)
        return
    
    for i in range(4):
        if ops[i] > 0:
            ops[i] -= 1
            if i == 0:
                back(idx + 1, total + arr[idx], ops)
            elif i == 1:
                back(idx + 1, total - arr[idx], ops)
            elif i == 2:
                back(idx + 1, total * arr[idx], ops)
            elif i == 3:
                if total < 0:
                    total = -(-total // arr[idx])
                else:
                    total //= arr[idx]
                back(idx + 1, total, ops)
            ops[i] += 1

back(1, arr[0], operations)

print(max_result)
print(min_result)