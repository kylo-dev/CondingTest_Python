from itertools import permutations

def calculate(op, a, b):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    
def solution(expression):
    answer = -float('inf')
    
    tokens = []
    num = ''
    for ch in expression:
        if ch.isdigit():
            num += ch
        else:
            tokens.append(int(num))
            tokens.append(ch)
            num = ''
    tokens.append(int(num))
    N = len(tokens)
    
    for ops in permutations(["+", "-", "*"]):
        temp_tokens = tokens[:]
        for op in ops:
            stack = []
            idx = 0
            while idx < len(temp_tokens):
                token = temp_tokens[idx]
                if token == op:
                    prev_num = stack.pop()
                    next_num = temp_tokens[idx + 1]
                    result = calculate(op, prev_num, next_num)
                    stack.append(result)
                    idx += 2
                else:
                    stack.append(token)
                    idx += 1
            temp_tokens = stack
            
        answer = max(answer, abs(temp_tokens[0]))
                
    return answer