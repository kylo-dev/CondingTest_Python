def solution(number, k):
    answer = []
    
    # 모든 숫자 문자열 탐색
    for digit in number:
        ### k가 0보다 크고, 배열 마지막 수가 탐색하는 수보다 큰지 확인
        while answer and k > 0 and answer[-1] < int(digit):
            answer.pop()
            k -= 1
        ### 아닌 경우, 배열에 숫자 더하기
        answer.append(int(digit))
    
    return "".join(map(str, answer[:len(number) - k]))