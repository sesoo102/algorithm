# 피자 굽기

'''
- 피자는 1번위치에서 넣거나 뺄 수 있다.
- 화덕 내부의 피자받침은 천천히 회전해서 1번에서 잠시 꺼내 치즈를 확인하고 다시 같은 자리에 넣을 수 있다.
- M개의 피자에 처음 뿌려진 치즈의 양이 주어지고, 화덕을 한 바퀴 돌 때 녹지않은 치즈의 양은 반으로 줄어든다. 이전 치즈의 양을 C라고 하면 다시 꺼냈을 때 C//2로 줄어든다.
- 치즈가 모두 녹아 0이 되면 화덕에서 꺼내고, 바로 그 자리에 남은 피자를 순서대로 넣는다.

첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50

다음 줄부터 테스트 케이스의 첫 줄에 화덕의 크기 N과 피자 개수 M이 주어지고, 다음 줄에 M개의 피자에 뿌려진 치즈의 양을 나타내는 Ci가 주어진다.

3<=N<=20, N<=M<=100, 1<=Ci<=20
'''
from collections import deque
T = int(input())

for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    cheases = [0] + list(map(int, input().split()))

    # 화덕 q
    q = deque()

    next_pizza = N + 1

    # i 피자번호
    for i in range(1, N+1):
        q.append((i, cheases[i]))
    
    while len(q) > 1:
        idx, chease = q.popleft()
        chease = chease // 2

        if chease > 0:
            q.append((idx, chease))
        
        else:
            if next_pizza <= M:
                q.append((next_pizza, cheases[next_pizza]))
                next_pizza += 1

    print(f'#{test_case} {q.pop()[0]}') 
