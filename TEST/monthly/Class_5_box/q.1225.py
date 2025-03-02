# 암호생성기

'''
다음 주어진 조건에 따라 n개의 수를 처리하면 8자리의 암호를 생성할 수 있다.

- 8개의 숫자를 입력 받는다.

- 첫 번째 숫자를 1 감소한 뒤, 맨 뒤로 보낸다. 

다음 첫 번째 수는 2 감소한 뒤 맨 뒤로, 그 다음 첫 번째 수는 3을 감소하고 맨 뒤로, 그 다음 수는 4, 그 다음 수는 5를 감소한다.

이와 같은 작업을 한 사이클이라 한다.

- 숫자가 감소할 때 0보다 작아지는 경우 0으로 유지되며, 프로그램은 종료된다. 이 때의 8자리의 숫자 값이 암호가 된다.
'''

from collections import deque

T = int(input())

for test_case in range(1, T+1):
    input()
    # 암호 q
    q = deque(map(int, input().split()))

    '''
    q.popleft()를 한 후  -1, -2, -3, -4, -5를 하고 q.append를 함.
    언제까지?
    q.popleft()를 한 후 마이너스를 하였을때 그 값이 0보다 작을때까지.
    '''


    while True:
        for i in range(1, 6):  
            num = q.popleft() - i  # 맨 앞 숫자 꺼내서 i만큼 감소
            if num <= 0:  # 0 이하가 되면 종료
                q.append(0)
                break
            q.append(num)  # 감소한 값 다시 추가
        else:
            continue  # 내부 for문이 정상 종료되면 while 반복 계속
        break  # 0 이하가 나오면 while문 종료
    
    print(f"#{test_case}", *q)

