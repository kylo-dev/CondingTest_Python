def solution(N, stages):
    answer = []
    
    ans = []
    for i in range(1, N+1):
        try_cnt = 0
        fail_cnt = 0
        for j in stages:
            if j >= i:
                try_cnt += 1
                if j == i:
                    fail_cnt += 1
        
        if fail_cnt == 0 or try_cnt == 0:
            ans.append((i, 0))
        else:
            ans.append((i, fail_cnt/try_cnt))
        
    
    ans.sort(key = lambda x: -x[1])
    for i in ans:
        answer.append(i[0])
    return answer