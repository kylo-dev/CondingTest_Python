
def solution(chicken):    
    answer = 0
    coupon = chicken
    
    while coupon >= 10:
        new_chicken = coupon // 10
        answer += new_chicken
        coupon = new_chicken + (coupon % 10)
    
    return answer
        
    