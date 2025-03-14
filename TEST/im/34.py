'''
3/4 IM 문제 복원
N명, 실력차이 K
팀구성, 최대 인원?

4   // testcase 수
4 2  // N, K
6 4 2 3  // 실력 숫자들    -> 3
4 3
1 2 3 4     -> 4
4 1
1 3 7 5     -> 1
24 7
28 8 21 13 7 13 27 17 29 5 12 28 29 19 16 1 23 21 13 9 15 5 24 12 -> 9?
'''


T = int(input())

for test_case in range(1, T+1):
    N, K = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    cnt = [0] * 1001
    for i in arr:
        cnt[i] += 1
    # print(cnt)
    
   
    max_value = -1
    for j in range(1, 1001-K):
        ans = 0
        for k in range(K+1):
            ans += cnt[j+k]
        # print(ans)

        
        if max_value < ans:
            max_value = ans
    
    print(max_value)


    '''
    진짜 이때 초집중 상태였나보다. 다음날 다시 풀어보려고 하니까 범위 조절이 엄청 헷갈린다.
    분명 어제는 한번에 풀었었는데...
    다시는 남지 않겠다는 의지 하나만으로 ㅋㅋㅋㅋㅋㅋ
    '''