import heapq

def solution(operations):
    
    min_heap = []
    max_heap = []
    
    for oper in operations:
        op, num = oper.split()
        num = int(num)
        
        if (op == "I"):
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        elif (op == 'D' and len(min_heap)):
            if num == 1:
                value = -heapq.heappop(max_heap)
                min_heap.remove(value)
            else:
                value = -heapq.heappop(min_heap)
                max_heap.remove(value)
    
    return [0, 0] if len(min_heap) == 0 else [-heapq.heappop(max_heap), heapq.heappop(min_heap)]