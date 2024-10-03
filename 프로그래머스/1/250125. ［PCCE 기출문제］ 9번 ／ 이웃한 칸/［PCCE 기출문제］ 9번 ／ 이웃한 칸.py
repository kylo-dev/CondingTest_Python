def solution(board, h, w):
    answer = 0
    N = len(board)
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    
    target = board[h][w]
    
    for i in range(4):
        nx = h + dx[i]
        ny = w + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if target == board[nx][ny]:
                answer += 1
    
    return answer