for test_case in range(1, 11):
    input()
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 도착 지점 x찾기.
    end_r = 99
    end_c = 0
    for j in range(100):
        if arr[99][j] == 2:
            end_c = j
    # X의 위치 = (r, c) = (99, end_c)
    # j-1, j+1 의 값이 1 인지  확인, 0이면 위로 이동

    while end_r != 0:
        #오른쪽 이동
        '''
        arr[end_r][end_c+1]에서 == 1을 명시하지 않은 이유
        보통 명확하게 arr[end_r][end_c+1] == 1 이라고 쓸 수도 있지만, 이 코드는 == 1을 생략한 형태.
        python에서는 숫자 조건문에서 0과 1이 False/True로 평가됨.
        즉, Python에서는 if 변수: 형태로 작성하면 변수 != 0일 때만 True로 판단해!
        따라서 arr[end_r][end_c+1]이 1이면 자동으로 조건이 True가 되고,
        0이면 False가 되므로 == 1을 생략해도 동일하게 동작한다.
        '''
        if 0 <= end_c+1 <= 99 and arr[end_r][end_c+1]:
            while end_c+1 <= 99 and arr[end_r][end_c+1]:
                end_c += 1
            end_r -= 1

        #왼쪽 이동
        elif 0 <= end_c-1 <= 99 and arr[end_r][end_c-1]:
            while end_c-1 <= 99 and arr[end_r][end_c-1]:
                end_c -= 1
            end_r -= 1

        else:
            end_r -= 1

    print(f"#{test_case} {end_c}")

    # https: // chaemi720.tistory.com / 22