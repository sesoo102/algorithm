# 숫자를 정렬하자 - 카운팅 정렬

T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    arr = list(map(int, input().split()))

    out = [0] * N # 주어진 배열과 비슷한 길이의 비어있는 배열을 만든다.
    # out: 정렬한 결과를 저장할 배열
    # len(arr) == N 이지만 함수를 쓰기보다 문제에서 주어진 입력값을 쓰도록 하자.

    #카운팅 정렬.
    # - 핵심 아이디어: 개수를 세서, 누적합을 하면 그 숫자의 상대적 위치를 알 수 있다.
    # - 카운팅 배열: COUNT[A] : A가 출연한 횟수
    # - 인덱스를 숫자로 활용
    # - 누적합 배열(Prefix sum) : 개수를 누적시켜 나감

    # 1. 카운팅 배열 만들기 <= 최댓값을 알아야 만들 수 있음.
    # 2. 누적합 배열 만들기
    # 3. 뒤에서부터 거꾸로 순회하면서 출력 배열에 "상대적 위치를 이용해" 채워 넣는다.

    # 최댓값 찾기
    max_val = arr[0]
    for i in range(1, N):
        if arr[i]>max_val:
            max_val = arr[i]
    # 1. 카운팅 배열
    cnt = [0]*(max_val + 1)

    # 숫자가 몇번 출연했는지 세기
    for i in range(N):
        cnt[arr[i]] += 1

    # 2. 누적합 배열
    for i in range(1, max_val+1):
        cnt[i] += cnt[i-1]

    # 3. 출력 배열에 넣기
    for i in range(N-1, -1, -1):

        out[cnt[arr[i]]-1] = arr[i]
        cnt[arr[i]] -= 1

    print(f'#{test_case} {" ".join([str(n) for n in out])}')











