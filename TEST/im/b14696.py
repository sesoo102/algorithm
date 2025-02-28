# 딱지놀이

'''
별4 > 동그라미3 > 네모5 > 세모1
무승부 D로 표기
'''

# 라운드 수
N = int(input())
for round in range(N):
    A_card = list(map(int, input().split()))
    B_card = list(map(int, input().split()))
    
    anum = A_card[0]
    bnum = B_card[0]
    acards = A_card[1:]
    bcards = B_card[1:]
    # print(acards)

    a_cnt = [0] * 5
    b_cnt = [0] * 5

    for a in acards:
        a_cnt[a] += 1
    
    for b in bcards:
        b_cnt[b] += 1

    # print(a_cnt)
    
    if a_cnt[4]>b_cnt[4]:
        print('A')
    elif a_cnt[4]<b_cnt[4]:
        print('B')
    else:
        if a_cnt[3]>b_cnt[3]:
            print('A')
        elif a_cnt[3]<b_cnt[3]:
            print('B')
        else:
            if a_cnt[2]>b_cnt[2]:
                print('A')
            elif a_cnt[2]<b_cnt[2]:
                print('B')
            else:
                if a_cnt[1]>b_cnt[1]:
                    print('A')
                elif a_cnt[1]<b_cnt[1]:
                    print('B')
                else:
                    print('D')


    # # 우선순위가 높은 모양(4 > 3 > 2 > 1)부터 비교
    # winner = 'D'  # 기본적으로 무승부로 설정
    # for shape in range(4, 0, -1):  # 4부터 1까지 감소하면서 비교
    #     if a_cnt[shape] > b_cnt[shape]:
    #         winner = 'A'
    #         break
    #     elif a_cnt[shape] < b_cnt[shape]:
    #         winner = 'B'
    #         break

    # print(winner)



    # # 우선순위가 높은 모양(4 > 3 > 2 > 1)부터 비교
    # winner = 'D'  # 기본적으로 무승부로 설정
    # for shape in range(4, 0, -1):  # 4부터 1까지 감소하면서 비교
    #     if a_cnt[shape] > b_cnt[shape]:
    #         winner = 'A'
    #     elif a_cnt[shape] < b_cnt[shape]:
    #         winner = 'B'

    #     # break 없이도 A나 B가 결정되었으면, 더 이상 변경되지 않음
    #     if winner != 'D':
    #         continue

    # print(winner)