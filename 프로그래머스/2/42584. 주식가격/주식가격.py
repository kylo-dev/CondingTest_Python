def solution(prices):
    N = len(prices)
    answer = [0 for _ in range(N)]
    
    stack = []
    
    for i in range(N):
        while stack and prices[stack[-1]] > prices[i]:
            top = stack.pop()
            answer[top] = i - top
        stack.append(i)

    for i in stack:
        answer[i] = N - i - 1
    
    return answer