import sys
input = sys.stdin.readline

N = int(input())
K = int(input())
sensors = sorted(list(map(int, input().split())))

diff = []

for i in range(N-1):
    diff.append(sensors[i + 1] - sensors[i])
diff.sort()

print(sum(diff[:N-K]))