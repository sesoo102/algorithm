T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    red = set()
    blue = set()

    for n in range(N):
        arr = list(map(int, input().split()))

        # 위치 좌표
        r1, c1, r2, c2, color = arr
        # 프로그래밍에선 r,j 사용. r은 세로 방향, j는 가로방향. 일반적인 x,y 좌표와는 반대이다.


        # 빨강 arr[-1] = 1
        if arr[-1] == 1:
            # (c, r)
            for c in range(c1, c2+1):
                for r in range(r1, r2+1):
                    red.add((c, r))
        # 파랑
        elif arr[-1] == 2:

            for c in range(c1, c2+1):
                for r in range(r1, r2+1):
                    blue.add((c, r))

        # 보라
    purple = red & blue

    print(f"#{test_case} {len(purple)}")