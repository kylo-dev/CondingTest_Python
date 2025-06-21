import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
arr = list(map(int, input().split()))
operations = map(int, input().split())

operation_dict = {"+": 0, "-":0, "*": 0, "//": 0}

for idx, oper in enumerate(operations):
    if idx == 0 and oper != 0:
        operation_dict["+"] += oper
    elif idx == 1 and oper != 0:
        operation_dict["-"] += oper
    elif idx == 2 and oper != 0:
        operation_dict["*"] += oper
    elif idx == 3 and oper != 0:
        operation_dict["//"] += oper

max_result = -float('inf')
min_result = float('inf')
def back(idx, total):
    global max_result, min_result
    if idx == len(arr) - 1:
        max_result = max(max_result, total)
        min_result = min(min_result, total)
        return

    for oper, cnt in operation_dict.items():
        if cnt > 0:
            operation_dict[oper] -= 1
            if oper == "+":
                back(idx + 1, total + arr[idx+1])
            elif oper == "-":
                back(idx + 1, total - arr[idx+1])
            elif oper == "*":
                back(idx + 1, total * arr[idx+1])
            elif oper == "//":
                if total < 0 :
                    total = -(-total // arr[idx+1])
                else:
                    total //= arr[idx+1]
                back(idx + 1, total)
            operation_dict[oper] += 1

back(0, arr[0])

print(max_result)
print(min_result)