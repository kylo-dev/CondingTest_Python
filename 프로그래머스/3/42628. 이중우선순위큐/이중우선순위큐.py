import heapq

def solution(operations):
    answer = []
    
    # 최댓값 제거, 최솟값 제거
    max_heap = []
    min_heap = []
    
    for op in operations:
        oper, num = op.split()
        
        if oper == "I":
            num = int(num)
            heapq.heappush(max_heap, (-num, num))
            heapq.heappush(min_heap, num)
        elif oper == "D" and len(min_heap):
            if num == "1":
                nums = heapq.heappop(max_heap)[1]
                min_heap.remove(nums)
            elif num == "-1":
                nums = heapq.heappop(min_heap)
                max_heap.remove((-nums, nums))
    
    if len(min_heap) == 0:
        return [0,0]
    else:
        return [heapq.heappop(max_heap)[1], heapq.heappop(min_heap)]