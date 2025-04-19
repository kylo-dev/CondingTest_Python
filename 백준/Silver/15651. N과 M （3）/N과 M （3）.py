
N, M = map(int, input().split())

ans = []

def back():
    global ans

    if len(ans) == M:
        print(' '.join(map(str, ans)))
        return

    for i in range(1, N + 1):
        ans.append(i)
        back()
        ans.pop()

back()