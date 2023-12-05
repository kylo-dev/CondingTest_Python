def divisor(n):
    cnt = 0
    if n == 1:
        return 1
    
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            cnt += 1
            
    if n**0.5 == int(n**0.5):
        return cnt * 2 - 1
    else:
        return cnt * 2

def solution(number, limit, power):
    weapon = []
    
    for i in range(1, number+1):
        cnt = divisor(i)
        if cnt <= limit:
            weapon.append(cnt)
        else:
            weapon.append(power)
    return sum(weapon)