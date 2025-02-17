# 수업내용
for test_case in range(1, 11):
    N = int(input())
    fx = input()
    # 후위표기식
    postfix = ''
    stack = [0] * N
    top = -1
    icp = {'(':3, '*':2, '/':2, '+':1, '-':1}
    isp = {'(':0, '*':2, '/':2, '+':1, '-':1}

    for x in fx:
        if x not in '(+-*/)':   # 피연산자
            postfix += x
        elif x == ')':      # '('까지 pop()
            while stack[top] != '(':    # peek
                postfix += stack[top]
                top -= 1
            top -= 1        # '(' 버림. pop
        else:   # '(+-*/'
            if top==-1 or isp[stack[top]] < icp[x]: # 토큰의 우선순위가 더 높으면
                top += 1    # push
                stack[top] = x
            elif isp[stack[top]] >= icp[x]:
                while top > -1 and isp[stack[top]] >= icp[x]:
                    postfix += stack[top]
                    top -= 1
                top += 1  # push
                stack[top] = x


    for x in postfix:
        if x not in '+-/*': # 피연산자이면
            # push(x)
            top += 1
            stack[top] = int(x)
        else:
            # pop()
            op2 = stack[top]
            top -= 1
            op1 = stack[top]
            top -= 1
            if x == '+':
                top += 1
                stack[top] = op1 + op2
            elif x == '-':
                top += 1
                stack[top] = op1 - op2
            elif x == '/':
                top += 1
                stack[top] = op1 / op2
            elif x == '*':
                top += 1
                stack[top] = op1 * op2
