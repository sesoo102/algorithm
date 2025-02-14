T = int(input())

for test_case in range(1, T + 1):
    arr = list(input())
    stack = [] 

    for char in arr:
        # 스택의 마지막 문자와 현재 문자가 같다면 제거
        if stack and stack[-1] == char:  
            stack.pop()
        else:
            # 다르면 추가
            stack.append(char)  

    print(f'#{test_case} {len(stack)}') 
