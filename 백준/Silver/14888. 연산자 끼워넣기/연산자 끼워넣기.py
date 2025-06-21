import sys
input = sys.stdin.readline

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
            next_ops = ops[:]
            next_ops[i] -= 1

            if i == 0:
                next_total = total + arr[idx]
            elif i == 1:
                next_total = total - arr[idx]
            elif i == 2:
                next_total = total * arr[idx]
            else:
                if total < 0:
                    next_total = -(-total // arr[idx])
                else:
                    next_total = total // arr[idx]
            
            back(idx + 1, next_total, next_ops)

back(1, arr[0], operations)

print(max_result)
print(min_result)