# 색칠하기

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [[0]*10 for _ in range(10)]
    for n in range(N):
        r1, c1, r2, c2, color = list(map(int, input().split()))

        if color == 1:
            for r in range(r1, r2+1):
                for c in range(c1, c2+1):
                    arr[r][c] +=1
        
        if color == 2:
            for r in range(r1, r2+1):
                for c in range(c1, c2+1):
                    arr[r][c] += 2
        
        cnt = 0
        for r in range(10):
            for c in range(10):
                if arr[r][c] == 3:
                    cnt +=1

    print(f"#{test_case} {cnt}")



