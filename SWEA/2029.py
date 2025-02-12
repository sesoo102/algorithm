T = int(input())
data = [input().split() for _ in range(T)]

result = []

for i in range(1, T+1):
    a, b = map(int, data[i - 1])
    result.append(f'#{i} {a // b} {a % b}')

print('\n'.join(result))