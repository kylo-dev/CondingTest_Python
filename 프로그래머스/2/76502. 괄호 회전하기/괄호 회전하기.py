def check(gal_str):
    
    stack = []
    for gal in gal_str:
        if not len(stack):
            stack.append(gal)
        elif gal == "(" or gal == "[" or gal == "{":
            stack.append(gal)
        elif gal == ")" and stack[-1] == "(":
            stack.pop()
        elif gal == "]" and stack[-1] == "[":
            stack.pop()
        elif gal == "}" and stack[-1] == "{":
            stack.pop()
    
    return True if not len(stack) else False

def solution(s):
    
    # len(s) - 1 만큼 회정
    # 올바른 괄호인 경우 +1
    
    # 올바른 괄호가 없는 경우 0 반환
    
    answer = 0
    
    for i in range(len(s) - 1):
        gal_str = s[i:] + s[:i]
        if check(gal_str):
            answer += 1
    return answer

