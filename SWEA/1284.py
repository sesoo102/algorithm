T = int(input())

# A사: 1리터당 P원의 돈을 내야 한다.

# B사 : 기본 요금이 Q원이고,
# 월간 사용량이 R리터 이하인 경우 요금은 기본 요금만 청구된다.
# 하지만 R 리터보다 많은 양을 사용한 경우 초과량에 대해 1리터당 S원의 요금을 더 내야 한다.

# W: 한달 사용하는 수도양
# 요금이 저렴한 회사를 선택하여 그 요금 출력

for test_case in range(1, T+1):
    p, q, r, s, w = list(map(int, input().split()))
    # a사 요금
    aw = p * w
    # b사 요금
    bw = q
    if w <= r:
        bw = q
    else:
        bw  += s*(w-r)
    
    if aw >= bw:
        print(f'#{test_case} {bw}')
    
    else:
        print(f'#{test_case} {aw}')