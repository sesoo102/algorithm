# 영화감독 숌

N = int(input())

count = 0  # 666이 포함된 숫자 개수 카운트
num = 666  # 666부터 시작

while True:
    if "666" in str(num):  # 현재 숫자에 '666'이 포함되어 있는지 확인
        count += 1  # 개수 증가
        if count == N:  # N번째 666 포함 숫자를 찾으면 종료
            print(num)
            break
    num += 1  # 다음 숫자로 이동
