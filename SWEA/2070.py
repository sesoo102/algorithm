T = input()
T = int(T)
testcase = []

for _ in range(T):
    a, b = list(map(int, input().split()))
    testcase.extend([a, b])

for i in range(0, len(testcase), 2):
    a, b= testcase[i], testcase[i+1]
    if a > b:
        print(f'#{i//2 + 1} >')
    elif a < b:
        print(f'#{i//2 + 1} <')
    else:
        print(f'#{i//2 + 1} =')




# for _ in range(T+1):
#     num = list(map(int, input().split()))
#     testcase.extend(num)

# for i in range(len(testcase)):
#     testcase[i]