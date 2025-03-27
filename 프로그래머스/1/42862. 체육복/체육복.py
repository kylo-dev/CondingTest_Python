def solution(n, lost, reserve):
    
    for r in reserve[:]:
        if r in lost:
            lost.remove(r)
            reserve.remove(r)
    
    for r in sorted(reserve):
        if r-1 in lost:
            lost.remove(r-1)
        elif r+1 in lost:
            lost.remove(r+1)
    
    return n - len(lost)