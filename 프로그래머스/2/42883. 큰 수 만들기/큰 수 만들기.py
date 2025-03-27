def solution(number, k):
    stack = []
    
    for digit in number:
        while stack and k > 0 and stack[-1] < digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    
    return "".join(stack[:len(number) - k])