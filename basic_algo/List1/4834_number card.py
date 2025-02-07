T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    given_number = int(input())
    number = []
    for _ in range(N):
        number.append(given_number % 10)
        given_number = given_number // 10
    # print(number) 입력받은 숫자를 리스트로 저장


    # number에서 최댓값 찾기
    max_num = number[0]
    for i in range(1, N):
        if number[i] > max_num:
            max_num = number[i]

    # 카운팅 배열
    cnt = [0]*(max_num+1)
    for i in range(N):
        cnt[number[i]] += 1

    # print(cnt) 구해하는 원 리스트 원소 중 최대값+1 만큼의 원소를 갖는(인덱스 번호와 숫자를 동일하게 매칭하기 위해) 배열을 만든 후 각 숫자가 얼만큼 있는지 표시.
    '''
    예를 들어 [1, 1, 1, 0, 0, 0, 0, 1, 1]
    인 경우 구하고자 하는 원 리스트의 원소 중 최댓값은 8이다.
    원 리스트에서 0은 1개, 1은 1개 등등 이 있다.
    원 리스트: [0, 8, 2, 7, 1]
    '''
    # cnt에서 최댓값 찾기
    max_cnt = cnt[0]
    for i in range(1, max_num+1):
        if max_cnt <= cnt[i]:
            max_cnt = cnt[i]

    # 같은 개수일 때 큰 숫자 찾기(거꾸로 탐색)
    frequent_number = -1
    for i in range(max_num, -1, -1):
        if cnt[i] == max_cnt:
            frequent_number = i
            break

# 가장 많은 카드에 적힌 숫자와 카드가 몇장인지 출력하는 프로그램. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력.
    print(f"#{test_case} {frequent_number} {max_cnt}")