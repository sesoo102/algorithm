T = int(input())

for test_case in range(1, T+1):
    sticks = list(map(str, input()))
    cnt = 0
    stack =[]

    for i in range(len(sticks)):
        if sticks[i] == '(':
            stack.append('(')
        elif sticks[i] == ')':
            if sticks[i-1] == '(':
                stack.pop()
                cnt += len(stack)
            else:
                stack.pop()
                cnt += 1
    print(f'#{test_case} {cnt}')