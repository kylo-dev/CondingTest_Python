import sys
input = sys.stdin.readline
import math

t = int(input())

for _ in range(t):
    west, east = map(int, input().split())

    print(math.comb(east, west))