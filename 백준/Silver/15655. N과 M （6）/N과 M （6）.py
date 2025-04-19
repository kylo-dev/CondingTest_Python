
N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

ans = []
def back(idx):

    if len(ans) == M:
        print(' '.join(map(str, ans)))
        return
    
    for i in range(idx, N):
        ans.append(arr[i])
        back(i + 1)
        ans.pop()


back(0)