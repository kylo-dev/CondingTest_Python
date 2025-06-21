from itertools import permutations

def calculate(a, b, op):
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
    
    for ops in permutations(["+", "-", "*"]):
        temp_tokens = tokens[:]
        
        for op in ops:
            idx = 0
            stack = []
            while idx < len(temp_tokens):
                token = temp_tokens[idx]
                if token == op:
                    _prev = stack.pop()
                    _next = temp_tokens[idx + 1]
                    result = calculate(_prev, _next, op)
                    stack.append(result)
                    idx += 2
                else:
                    stack.append(token)
                    idx += 1
            temp_tokens = stack
                    
        answer = max(answer, abs(temp_tokens[0]))
        
    return answer