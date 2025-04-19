def solution(elements):
    ans = set()
    N = len(elements)
    
    for i in range(1, N + 1):
        for j in range(N):
            total = sum(elements[j:j+i])
            if j + i >= N:
                total += sum(elements[:j+i-N])
            ans.add(total)
    
    return len(ans)
    