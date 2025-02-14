T = int(input())

for test_case in range(1, T + 1):
    string = list(input())  # 문자열을 리스트로 변환
    i = 0  # 인덱스 초기화

    while i < len(string) - 1:  # 리스트 범위 내에서 탐색
        if string[i] == string[i + 1]:  # 연속된 문자가 같다면
            string.pop(i)  # 현재 문자 제거
            string.pop(i)  # 다음 문자 제거 (같은 인덱스)
            i = max(0, i - 1)  # 이전 문자부터 다시 확인 (범위 벗어나지 않게)
        else:
            i += 1  # 다음 문자로 이동

    print(f'#{test_case} {len(string)}')
