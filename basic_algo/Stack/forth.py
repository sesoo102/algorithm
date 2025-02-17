T = int(input())
for test_case in range(1, T + 1):
    postfix = input().split()  
    stack = []
    
    for x in postfix:
        if x not in '+-/*':
            stack.append(int(x))
        elif x in '+-/*':
            op2 = stack.pop()
            op1 = stack.pop()

            if x == '+':
                stack.append(op1 + op2)
            elif x == '-':
                stack.append(op1 - op2)
            elif x == '/':
                if op2 == 0:  # 0 나누기 x
                    print("error")
                else:
                    stack.append(op1 // op2)  # 정수 나눗셈
            elif x == '*':
                stack.append(op1 * op2)
        else:
            print('error')
    
   
    if len(stack) == 1:
        print(stack.pop()) 
    else:
        print("error")            