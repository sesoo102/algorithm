# 수열

'''
단순합계로 구하면 시간초과가 발생한다.
# N 온도를 측정한 전체 날짜, K 연속적인 날짜의 수
N, K = list(map(int, input().split()))
temperature = list(map(int, input().split()))

max_value = -999999999
for n in range(N-K+1):
    sum_temp = 0
    for k in range(K):
        sum_temp += temperature[n+k]
        if max_value < sum_temp:
            max_value = sum_temp

print(max_value)
'''

# 누적합
N, K = map(int, input().split())
temperature = list(map(int, input().split()))

# 첫 K일의 합을 수동으로 계산
current_sum = 0
for i in range(K):
    current_sum += temperature[i]

max_value = current_sum

# 슬라이딩 윈도우 적용
'''
매번 첫 번째 값을 빼고 마지막 값을 더하는 방식
'''
for n in range(1, N - K + 1):
    current_sum = current_sum - temperature[n - 1] + temperature[n + K - 1]
    if current_sum > max_value:
        max_value = current_sum

print(max_value)
