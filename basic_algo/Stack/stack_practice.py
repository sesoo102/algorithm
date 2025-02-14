T = int(input())

for test_case in range(1, T+1):
    arr = list(input())
    stack = []
    ans = 1

    for a in arr:
        if a =='(' or a == '{':
            stack.append(a)
        elif a == ')':
            if not stack or stack[-1] != '(':
                ans = 0
                break
            else:
                stack.pop()
        elif a == '}':
            if not stack or stack[-1] != '{':
                ans = 0
                break 
            else:
                stack.pop()

    
    
    if stack:
        ans = 0
    
    print(f"#{test_case} {ans}")
            
