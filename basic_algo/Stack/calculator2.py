for test_case in range(1, 11):
    N = int(input())
    fx = input().strip()

    # 후위표기식
    postfix = ''
    stack = []

    for x in fx:
        if x not in '+*':
            postfix += x
        
        elif x == '*':
            if not stack or stack[-1] =='+':
                stack.append(x)
            else:
                while stack and stack[-1] == '*':
                    postfix += stack.pop()
                stack.append(x)
        
        elif x == '+':
            while stack:
                postfix += stack.pop()
            stack.append(x)
    
    while stack:
        postfix += stack.pop()
                
    ans =[]

    for x in postfix:
        if x not in '+*':
            ans.append(int(x))
        
        else:
            op2 = ans[-1]
            ans.pop()
            op1 = ans[-1]
            ans.pop()
            if x == '+':
                ans.append(op1 + op2)
            elif x == '*':
                ans.append(op1 * op2)
            
    print(f"#{test_case} {ans.pop()}")