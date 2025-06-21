import heapq, sys
input = sys.stdin.readline

N = int(input())
max_heap =[]

for _ in range(N):
    num = int(input())

    if num != 0:
        heapq.heappush(max_heap, (-num, num))
    
    if num == 0:
        if max_heap:
            nums = heapq.heappop(max_heap)
            print(nums[1])
        else:
            print(0)
