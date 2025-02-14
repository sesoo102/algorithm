T = int(input())

for test_case in range(1, T+1):
    arr = list(input().strip())
    m = len(arr)
    n_arr = [int(arr[i]) for i in range(m)]
    # arr[i] 기립 박수를 하고 있는 사람이 i명 이상일때 기립 박수를 하는 사람의 수.
    # arr[-1] != 0
    

    # 필요한 사람수
    need = 0
    # 박수 치고 있는 사람수
    clap = 0
    
    for i in range(m):
        if n_arr[i] > 0:
            if clap < i:  # 필요한 사람보다 박수치는 사람이 적으면 추가
                need += (i - clap)
                clap = i  # 추가된 사람도 함께 고려
            clap += n_arr[i]  # 현재 위치의 사람들 포함
    
    print(f'#{test_case} {need}')