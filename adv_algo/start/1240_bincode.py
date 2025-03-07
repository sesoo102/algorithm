T = int(input())

for test_case in range(1, T+1):
    # N 세로 크기, M 가로 크기
    N, M = map(int, input().split())

    # 2차원 배열 입력 받기
    arr = [list(input().strip()) for _ in range(N)]
    
    binary_code = ''  # 암호 코드 저장 변수

    # 암호 코드 찾기
    for r in range(N):
        for c in range(M-1, -1, -1):  # 뒤에서부터 찾기
            if arr[r][c] == '1':  # 1을 찾으면 해당 줄에서 56개 추출
                binary_code = ''.join(arr[r][c-55:c+1])  # 56자리 코드 추출
                break
        if binary_code:
            break  # 코드 찾으면 루프 종료
    
    print(binary_code)
