'''
각 분반은 원활한 교육을 위해 최소인원 이상과 최대 인원 이하를 만족.
임의로 3개의 분반으로 나누엇을 때 학생이 가장 많은 분반과 적은 분반의 학생 수 차이의 최솟값 출력.
분반을 조건에 맞춰서 나눌 수 없다면 -1 출력.
'''

"""
score1이 1~100일때 score2rk score1~100 일때 모든 경우의 수 확인
"""
T = int(input())  # 테스트 케이스 개수 입력

for test_case in range(1, T+1):
    # 학생 수 N, 최소 인원 min_n, 최대 인원 max_n
    N, min_n, max_n = map(int, input().split())
    scores = list(map(int, input().split()))  # 학생들의 점수 리스트

    cnt = [0] * 101  # 점수별 학생 수 카운트 배열

    for i in scores:
        cnt[i] += 1  # 각 점수별 학생 수 저장

    # 가능한 최솟값을 구하기 위한 변수
    answer = 999999999  # 최솟값을 찾기 위해 큰 값으로 초기화

    # 첫 번째 분반 (a)의 끝을 i로 설정
    for i in range(101):
        a = 0  # 첫 번째 분반의 학생 수

        # 첫 번째 분반의 학생 수 합산
        for x in range(i):
            a += cnt[x]

        # 최소 인원, 최대 인원 만족 확인
        if a < min_n or a > max_n:
            continue

        # 두 번째 분반 (b)의 끝을 j로 설정
        for j in range(i + 1, 101):
            b = 0  # 두 번째 분반의 학생 수

            # 두 번째 분반의 학생 수 합산
            for y in range(i, j):
                b += cnt[y]

            # 최소 인원, 최대 인원 만족 확인
            if b < min_n or b > max_n:
                continue

            # 세 번째 분반 (c)의 학생 수
            c = 0
            for z in range(j, 101):
                c += cnt[z]

            # 최소 인원, 최대 인원 만족 확인
            if c < min_n or c > max_n:
                continue

            # 최댓값과 최솟값 찾기 (내장함수 없이)
            max_value = a  # 임시로 최댓값을 a로 설정
            min_value = a  # 임시로 최솟값을 a로 설정

            if b > max_value:
                max_value = b
            if c > max_value:
                max_value = c

            if b < min_value:
                min_value = b
            if c < min_value:
                min_value = c

            # 최솟값 업데이트
            if answer > max_value - min_value:
                answer = max_value - min_value

    # 가능한 분할이 없으면 -1 출력
    if answer == 999999999:
        answer = -1

    print(f"#{test_case} {answer}")  # 결과 출력
