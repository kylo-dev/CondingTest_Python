import sys, heapq
input = sys.stdin.readline

N = int(input())
classes = []

for _ in range(N):
    classes.append(list(map(int, input().split())))

classes.sort(key = lambda x: x[0])

class_heap = []

for start, end in classes:
    if not class_heap:
        heapq.heappush(class_heap, end)
        continue
    
    if class_heap:
        if start < class_heap[0]:
            heapq.heappush(class_heap, end)
        else:
            heapq.heappop(class_heap)
            heapq.heappush(class_heap, end)


print(len(class_heap))