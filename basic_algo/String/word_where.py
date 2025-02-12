T = int(input())

def cnt_vh(n, k, a):
    # (r, c) r-> c 순서. r이 세로, c가 가로.
    # 1이 K개 있는 위치 찾기.
    result = 0 

    for i in range(n):
        sum = 0
        
        #가로
        for j in range(n):
            if arr[i][j] == 1:
                sum += 1
            if arr[i][j] == 0 or j == n-1:
                if sum == k:
                    result += 1
                sum = 0 
                
		#세로
        for j in range(n):
            if arr[j][i] == 1:
                sum += 1
            if arr[j][i] == 0 or j == n-1:
                if sum == k:
                    result+=1
                sum = 0
 
    return result

for tc in range(1, T+1):
    # N*N 크기 단어 퍼즐, K: 단어의 길이
    N, K = list(map(int, input().split()))
    # 1: 흰색, 0: 검은색
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    print(f"#{tc} {cnt_vh(N, K, arr)}")