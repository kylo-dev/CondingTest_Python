def solution(triangle):
    answer = 0
    
    # 밑바닥 인덱스
    floor = len(triangle) - 1
    
    while floor > 0:
        for i in range(floor):
            triangle[floor - 1][i] += max(triangle[floor][i], triangle[floor][i + 1])
        floor -= 1
    
    return triangle[0][0]