def find_binary(binary):
    # 이진수에서 1의 개수가 K개인 작은 이진수를 찾는다
    # 시작-끝 무조건 1
    global N, K

    # 파라미터 초기화
    L = len(binary)
    max_length = 0

    # 알고리즘
    # 인덱스 하나를 시작으로
    # 1의 개수를 센다
    for idx in range(0, L):

        # 1의 개수 초기화
        num1 = 0

        # 현재 인덱스가 1이라면
        if binary[idx] == "1":
            # 현재 인덱스 기준으로 시작
            for i in range(idx, L):
                # print(binary[idx:i+1])
                # 1의 개수를 센다
                if binary[i] == "1":
                    num1 += 1

                # 1의 개수가 K개라면 길이를 구하고
                if num1 == K:
                    # 최대 길이를 갱신한다
                    if max_length < (i - idx) + 1:
                        max_length = i - idx + 1
                    break

    # 최대값 반환
    return max_length


T = int(input())

for t in range(1, T + 1):
    # N자리 이진수, 1인 자리를 K개 가지고 있다
    N, K = list(map(int, input().split()))

    # 이진수 받기: str 형태
    binary = input()

    # 최대 길이 구하기
    max_l = find_binary(binary)

    # 결과 출력
    print(f"#{t} {max_l}")
