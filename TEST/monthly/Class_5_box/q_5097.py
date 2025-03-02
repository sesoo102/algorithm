# 회전
'''
3
3 10
5527 731 31274
5 12
18140 14618 18641 22536 23097
10 23
17236 31594 29094 2412 4316 5044 28515 24737 11578 7907
'''

T = int(input())
for test_case in range(1, T+1):
    # N개의 숫자, 작업 M번 반복
    N, M = list(map(int, input().split()))

    
    q = list(map(int, input().split()))

    for m in range(M):
        q.append(q.pop(0))
    
    print(f"# {test_case} {q.pop(0)}")