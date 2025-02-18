T = int(input()) 


def winner(l, r):
    global cards

    # 기저 조건
    # 구간의 길이가 1일 때
    if l == r:
        return l
    
    mid = (l + r) // 2
    l_win = winner(l, mid)
    r_win = winner(mid+1, r)

    if cards[l_win] == cards[r_win]:
        return l_win
    
    if cards[l_win] == 1:
        if cards[r_win] == 2:
            return r_win
        elif cards[r_win] == 3:
            return l_win
    elif cards[l_win] == 2:
        if cards[r_win] == 1:
            return l_win
        elif cards[r_win] == 3:
            return r_win	
    elif cards[l_win] == 3:
        if cards[r_win] == 1:
            return r_win
        elif cards[r_win] == 2:
            return l_win


for test_case in range(1, T+1):
    N = int(input())
    cards = [0] + list(map(int, input().split()))

    # 구간
    # [i, j] 구간이라면
    # [i, (i+j)//2], [(i+j)//2+1, j]

    num = winner(1, N) # [1, N] 구간의 승자의 번호

    print(f'#{test_case} {num}')