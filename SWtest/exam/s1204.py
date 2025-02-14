# 최빈수 구하기
T = int(input())
for test_case in range(1, T+1):
    input()
    score = list(map(int, input().split()))
    # 학생수
    n = 1000
    arr = [0] * 101

    for sc in score:
        arr[sc] += 1

    max_idx = 0
    for i in range(101):
        if arr[max_idx] <= arr[i]:
            max_idx = i
    
    print(f'#{test_case} {max_idx}')