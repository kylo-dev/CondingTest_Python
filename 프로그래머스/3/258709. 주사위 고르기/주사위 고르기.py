from itertools import combinations, product

def solution(dice):
    
    N = len(dice)
    best_win_count = 0
    all_cases = list(combinations(range(N), N//2))
    
    sum_comb = []
    for case in all_cases:
        selected_dice = [dice[idx] for idx in case]
        possible_sums = sorted(sum(rolls) for rolls in product(*selected_dice))
        sum_comb.append(possible_sums)
        
    num_cases = len(sum_comb)
    
    # A vs B
    for i in range(num_cases):
        a_sums = sum_comb[i]
        b_sums = sum_comb[num_cases - i - 1]
        
        win_count = 0
        
        for a in a_sums:
            left, right = 0, len(b_sums) - 1
            
            while left <= right:
                mid = (left + right) // 2
                if b_sums[mid] < a:
                    left = mid + 1
                else:
                    right = mid - 1
                
            win_count += left
        
        if win_count > best_win_count:
            best_win_count = win_count
            best_comb = [idx + 1 for idx in all_cases[i]]
        
    return best_comb