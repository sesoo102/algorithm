# 주사위 쌓기

'''
아래서부터 1번 주사위, 2번 주사위 ...
규칙!
서로 붙어 있는 두 개의 주사위에 붙어있는 면의 숫자는 같아야한다.
쌓아 올린 사각기둥의 한 옆면의 숫자의 합이 최댓값을 구하여라

    A
B   C   D   E
    F
'''
N = int(input())

dice_list = []  # 주사위 정보 저장
for _ in range(N):
    dice = list(map(int, input().split()))
    dice_list.append(dice)

# 주사위의 마주 보는 면을 찾기 위한 인덱스 매핑 (A, B, C, D, E, F)
opposite = [5, 3, 4, 1, 2, 0]  # 마주 보는 면의 인덱스

max_sum = 0  # 최대 옆면 합

# 첫 번째 주사위의 윗면을 모든 경우(6가지)로 시도
for i in range(6):
    bottom = dice_list[0][i]  # 첫 번째 주사위 아랫면
    top = dice_list[0][opposite[i]]  # 첫 번째 주사위 윗면
    
    total = 0  # 옆면 숫자 합
    for j in range(N):
        # 현재 주사위에서 아랫면과 윗면을 제외한 4개 숫자 중 최댓값 찾기
        side_max = 0
        for k in range(6):
            if dice_list[j][k] != bottom and dice_list[j][k] != top:
                if dice_list[j][k] > side_max:
                    side_max = dice_list[j][k]
        total += side_max  # 최댓값 누적

        # 다음 주사위의 아랫면, 윗면 업데이트
        if j < N - 1:
            for k in range(6):
                if dice_list[j + 1][k] == top:
                    bottom = dice_list[j + 1][k]
                    top = dice_list[j + 1][opposite[k]]
                    break
    
    if total > max_sum:
        max_sum = total

print(max_sum)





