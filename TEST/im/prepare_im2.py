'''
led는 4행행
LED 각 픽셀은 1(on), 0(off) 2가지 상태를 가지며 일정한 주기로 다음과 같이 변한다.
(i,j)는 i열, j행
i+j+1이 시간 k의 배수이며 다른 상태로 바뀜
시간 k=0일때 모두 0

가로크기 n, 시간 k, 1 상태의 픽셀의 갯수
n=5 K=3 10
'''
"""
4
5 3
35 39
93 70
569 138

10
20
123
1175
"""

T = int(input())
for test_case in range(1, T+1):
    N, K = list(map(int, input().split()))

    arr = [[0]*N for _ in range(4)]
    

    for k in range(1, K+1):
        for i in range(4):
            for j in range(N):
                if (i+j+1) % k == 0:
                    arr[i][j] = (arr[i][j]+1)%2

    # print(arr)

   
    
    cnt = 0
    for i in range(4):
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
    
    print(f"#{test_case} {cnt}")
