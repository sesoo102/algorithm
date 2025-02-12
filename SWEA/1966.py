T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 버블 정렬
    for i in range(N-1):
        for j in range(N -1 -i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print(f'#{test_case}', *arr)

    # 카운팅 정렬
    # 1. 최댓값 찾기(카운팅 배열 크기 결정정)
    max_val = max(arr)

    # 2. 카운트 배열 초기화
    count = [0]*(max_val +1)

    # 3. 카운트 배열 채우기
    for num in arr:
        count[num] += 1
    
    # 4. 정렬된 결과 생성
    sorted_arr = []
    for num in range(len(count)):
        sorted_arr.extend([num]*count[num]) # 카운트 개수만큼 숫자 추가
    
    print(f'#{test_case}', *sorted_arr)