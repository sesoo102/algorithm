# 숫자 카드

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().strip()))

    # print(cards)

    cnt = [0]* (10)

    for i in cards:
        cnt[i] += 1

    max_idx = 0
    for j in range(10):
        if cnt[max_idx] <= cnt[j]:
            max_idx = j

    print(f'#{test_case} {max_idx} {cnt[max_idx]}')