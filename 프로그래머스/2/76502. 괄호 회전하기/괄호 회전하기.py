def col_str(s):
    stk = []
    for i in s:
        if not stk:
            if i == ')' or i == '}' or i == ']':
                return False
            stk.append(i)
        else:
            if i == ')' and stk[-1] == '(':
                stk.pop()
            elif i == '}' and stk[-1] == '{':
                stk.pop()
            elif i == ']' and stk[-1] == '[':
                stk.pop()
            else:
                stk.append(i)
                
    return len(stk) == 0

def solution(s):
    answer = 0
    for i in range(len(s)):
        new_s = s[i:] + s[:i]
        if col_str(new_s):
            answer += 1
    return answer