import heapq

def solution(food_times, k):
    
    if sum(food_times) <= k:
        return -1
    
    q = []
    sum_value = 0
    prev = 0
    length = len(food_times)
    for i in range(length):
        # 우선순위 큐에 음식 시간과 음식 번호를 주입
        heapq.heappush(q, (food_times[i], i+1))
    
    while sum_value + ((q[0][0] - prev) * length) <= k:
        now = heapq.heappop(q)[0] # 현재 음식 시간
        sum_value += (now - prev) * length
        length -= 1 # 다 먹은 음식 제외
        prev = now # 이전 음식의 시간으로 설정
    
    result = sorted(q, key = lambda x: x[1])
    return result[(k-sum_value) % length][1]
    