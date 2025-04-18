def solution(brown, yellow):
    
    yel_x, yel_y = 0, 0
    
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            yel_x = yellow // i
            yel_y = i

            if (yel_x * 2) + (yel_y * 2) + 4 == brown:
                ans = [yel_x + 2, yel_y + 2]
                return sorted(ans, reverse=True)