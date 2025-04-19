
N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

ans = []
def back():

    if len(ans) == M:
        print(' '.join(map(str, ans)))
        return
    
    for i in range(N):
        ans.append(arr[i])
        back()
        ans.pop()


back()