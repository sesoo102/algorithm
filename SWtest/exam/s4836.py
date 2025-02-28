T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    # 빈 캔버스 만들기
    arr = [[0]*10 for _ in range(10)]

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
    
    # 사각형에 색칠하기
    for r in range(r1, r2+1):
        for c in range(c1, c2+1):
            arr[r][c] += color
    
    # area ==3 인 부분 찾기
    area = 0
    for r in range(10):
        for c in range(10):
            if arr[r][c] == 3:
                area += 1
    
    print(f'#{test_case} {area}')