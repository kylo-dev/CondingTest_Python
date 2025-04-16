import heapq
def solution(jobs):
    
    jobs = sorted([(req, dur, idx) for idx, (req, dur) in enumerate(jobs)])
    heap = []
    N = len(jobs)
    time, total_wait, idx = 0, 0, 0
    
    while idx < N or heap:
        while idx < N and jobs[idx][0] <= time:
            req, dur, job_id = jobs[idx]
            heapq.heappush(heap, (dur, req, job_id))
            idx += 1
        
        if heap:
            dur, req, job_id = heapq.heappop(heap)
            time += dur
            total_wait += time - req
        else:
            time = jobs[idx][0]
    return total_wait // N
    