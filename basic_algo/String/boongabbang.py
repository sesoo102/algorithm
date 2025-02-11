T = int(input())

# N명의 사람, M초의 시간을 들이면 K개의 붕어빵

for tc in range(1,T+1):
    N, M, K = list(map(int, input().split()))
    times = list(map(int, input().split()))

    cnt = [0]*11112

    for time in times:
        cnt[time]+=1

    ans = 'Possible'
    breads = 0

    for t in range(0, 11112):
        if t != 0 and t % M == 0:
            breads += K
        
        if cnt[t] > breads:
            ans = 'impossible'
            break

        breads -= cnt[t]

    
    print(f'#{tc} {ans}')



