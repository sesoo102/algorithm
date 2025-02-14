# n명, m번 공받으면 끝, 자신의 횟수가 홀수시 시계방향으로 l번째, 짝수 반시계 l번째째
n, m, l = list(map(int, input().split()))
# 공던진 횟수
cnt = 0

arr = [0] * n
idx = 0
while True:
    arr[idx] += 1
    if arr[idx] == m:
        print(cnt)
        break
    
    elif arr[idx] % 2 != 0:
        idx = (idx + l) % n
    else:
        idx = (idx + n - l) % n
    cnt += 1