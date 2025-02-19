from collections import deque

for test_case in range(1, 11):
    input()  
    q = deque(map(int, input().split())) 

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

    print(f"#{test_case} {' '.join(map(str, q))}")
