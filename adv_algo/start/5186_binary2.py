# 이진수2

T = int(input())
for test_case in range(1, T+1):
    N = float(input())
    # print(N)
    binary_number = ''
    while N > 0:
        N *= 2

        if N >= 1:
            binary_number += '1'
            N -= 1
        else:
            binary_number += '0'
        
        if len(binary_number) >= 13:
            binary_number = 'overflow'
            break

    print(f"#{test_case} {binary_number}")



















# T = int(input())  # 테스트 케이스 개수

# for test_case in range(1, T + 1):
#     N = float(input())  # 입력값 (소수)

#     binary_number = ''
    
#     while N > 0:
#         if len(binary_number) > 12:  # 13번째 비트가 되면 overflow
#             binary_number = "overflow"
#             break

#         N *= 2  # 2를 곱함

#         if N >= 1:
#             binary_number += '1'
#             N -= 1  # 정수 부분 제거
#         else:
#             binary_number += '0'

#     print(f"#{test_case} {binary_number}")  # 결과 출력

