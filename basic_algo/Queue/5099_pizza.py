from collections import deque

T = int(input())
for test_case in range(1, T+1):
    # N 화덕의 크기, M 피자 개수.
    N, M = list(map(int, input().split()))
    C = [0] + list(map(int, input().split()))

    # 화덕 q
    q = deque()

    next_pizza = N+1

    # i 피자번호
    for i in range(1,N+1):
        q.append((i, C[i]))
    
    while len(q) > 1:
        idx, cheese = q.popleft()
        cheese = cheese // 2

        if cheese > 0:
            q.append((idx, cheese))
        else:
            if next_pizza < M+1:
                q.append((next_pizza, C[next_pizza]))
                next_pizza += 1          
    

    
    print(f'#{test_case} {q.pop()[0]}')            