T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    for n in range(N):
        for i in range(n+1):
            if i == 0 or i == n:
                arr[n][i] = 1
            
            else:
                arr [n][i] = arr[n-1][i-1] + arr[n-1][i]
                
        while arr[n][-1] == 0:
            arr[n].pop()
        


    print(f'#{test_case}')
    for n in range(N):
        print(' '.join(map(str, arr[n])))  # 리스트를 공백으로 구분하여 출력
    

