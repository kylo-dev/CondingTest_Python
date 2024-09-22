import bisect

N = int(input())
arr = list(map(int, input().split()))

dp = []

for num in arr:
    pos = bisect.bisect_left(dp, num)
    
    if pos < len(dp):
        dp[pos] = num  # 해당 위치의 값을 업데이트
    else:
        dp.append(num)  # 배열의 끝에 추가

print(len(dp))
