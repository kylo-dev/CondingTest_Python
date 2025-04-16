from heapq import heappop, heappush

def solution(jobs):

    jobs = sorted([(req, dur, idx) for idx, (req, dur) in enumerate(jobs)])
    
    time, total_wait, idx = 0, 0, 0
    N = len(jobs)
    heap = []
    
    while idx < N or heap:
        while idx < N and jobs[idx][0] <= time:
            req, dur, job_id = jobs[idx]
            heappush(heap, (dur, req))
            idx += 1
        
        if heap:
            dur, req = heappop(heap)
            time += dur
            total_wait += time - req
        else:
            time = jobs[idx][0]
    
    return total_wait // N
            