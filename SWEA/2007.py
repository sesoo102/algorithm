T = int(input())

for test_case in range(1, T+1):
    string = input()
    # 마디의 길이 후보
    p = 1

    while p <= 10:
        # 현재 p가 유효한 마디인지 확인하는 변수
        valid = True
        for i in range(30-p):
            if string[i] != string[i+p]:    # 마디가 꺠지면
                valid = False   # 유효하지 않은 마디
                break
        if valid:   # valid가 true라면(=모든 비교가 성공했다면)
            break   # 정답을 찾았으므로 while 루프를 종료
        
        p += 1  # 유효하지 않으면 다음 길이의 마디를 확인

        
    print(f"#{test_case} {p}")



# 문자열 슬라이싱 방법
T = int(input())

for test_case in range(1, T+1):
    string = input()

    # 마디 길이 찾기
    for p in range(1, 11):  # 마디 길이는 1부터 10까지 가능
        pattern = string[:p]  # 마디 후보 (첫 p개 문자)
        valid = True  # 마디 여부 확인 변수

        # 마디 길이(p) 단위로 반복되는지 확인
        for i in range(p, 30, p):  # p 간격으로 이동하면서 검사
            if string[i:i + p] != pattern:  # 다음 부분이 동일한지 확인
                valid = False
                break
        
        if valid:  # 반복되는 마디를 찾으면 종료
            print(f"#{test_case} {p}")
            break
