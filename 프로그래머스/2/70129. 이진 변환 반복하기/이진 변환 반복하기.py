def solution(s):
    answer = []

    del_cnt = zero_cnt = 0

    while s != '1':
        # 0 제거
        zero_cnt += s.count('0')
        s = s.replace('0', '')

        # 이진 변환
        s = bin(len(s))
        s = s.replace('0b', '')
        del_cnt += 1

    answer.append(del_cnt)
    answer.append(zero_cnt)
    return answer