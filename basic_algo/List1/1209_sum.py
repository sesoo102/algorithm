T = 10
my_list=[]

for test_case in range(1, T+1):
    input()
    arr = [list(map(int, input().split())) for _ in range(100)]

# (i, j)

    for i in range(100):
        s1 = 0
        for j in range(100):
            s1 += arr[i][j]
        my_list.append(s1)

    for j in range(100):
        s2 = 0
        for i in range(100):
            s2 += arr[i][j]
        my_list.append(s2)

    s3=0
    for i in range(100):
        s3 += arr[i][i]
    my_list.append(s3)

    s4=0
    for i in range(100):
        s4 += arr[i][99-i]
    my_list.append(s4)

    print(f'#{test_case} {max(my_list)}')