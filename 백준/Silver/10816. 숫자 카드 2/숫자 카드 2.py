import sys
input = sys.stdin.readline
from collections import Counter


N = int(input())
card_num = list(map(int, input().split()))

card_count = dict(Counter(card_num))

M = int(input())
check_num = list(map(int, input().split()))

for check in check_num:
    if check in card_count:
        print(card_count[check], end=" ")
    else:
        print(0, end=" ")