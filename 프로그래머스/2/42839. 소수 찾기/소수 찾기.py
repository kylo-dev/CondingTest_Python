from itertools import permutations

def is_prime(x):
    if x < 2:
        return False
    
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    prime_set = set()
    
    for i in range(1, len(numbers) + 1):
        for perm in permutations(numbers, i):
            check = int(''.join(perm))
            
            if is_prime(check):
                prime_set.add(check)
    
    return len(prime_set)