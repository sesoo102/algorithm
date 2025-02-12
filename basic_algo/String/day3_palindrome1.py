# 출력 형식 백만번 확인하자!!

# 다른사람
for test_num in range(1,11):
    n=int(input())
    lst=[]
    for _ in range(8):
        lst.append(list(input()))
    cnt=0
    lst2=list(zip(*lst))
    for i in range(8):
        for j in range(8-n+1):
            if lst[i][j:j+n]==lst[i][j:j+n][::-1]:
                cnt+=1
            if lst2[i][j:j+n]==lst2[i][j:j+n][::-1]:
                cnt+=1
    print(f"#{test_num} {cnt}")

# 처음
for tc in range(1, 11):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(8)]
    cnt = 0
    middle_idx = N //2

    # 가로
    for i in range(8):
        for j in range(8-N+1):
                for k in range(middle_idx):
                    if arr[i][j+k] != arr[i][N+j-1-k]:
                        break
                else:
                    cnt += 1

    # 세로
    for j in range(8):
        for i in range(8-N+1):
            for k in range(middle_idx):
                if arr[i+k][j] != arr[N+i-1-k][j]:
                    break
            else:
                cnt += 1
    
    print(f"#{tc} {cnt}")

# 두번째째
for tc in range(1, 11):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(8)]
    cnt = 0
    middle_idx = N //2

    # 가로
    for i in range(8):
        for j in range(8-N+1):
                for k in range(middle_idx):
                    if arr[i][j+k] != arr[i][N+j-1-k]:
                        break
                else:
                    cnt += 1

    # 세로
    for j in range(8):
        for i in range(8-N+1):
            for k in range(middle_idx):
                if arr[i+k][j] != arr[N+i-1-k][j]:
                    break
            else:
                cnt += 1
    
    print(f"#{tc} {cnt}")