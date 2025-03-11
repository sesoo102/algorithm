N = int(input())
result = 0

for n in range(1, N):
    m = 0
    temp = n  # 원래 숫자를 저장

    while temp > 0:
        m += temp % 10
        temp //= 10

    if n + m == N:
        result = n
        break

print(result)
