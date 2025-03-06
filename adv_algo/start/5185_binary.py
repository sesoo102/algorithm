# 이진수
'''
N 자리 16진수 > 2진수
맨 앞 0 도 출력
'''

T = int(input())

hex_bin= {
    '0': '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111',
    }
for test_case in range(1, T+1):
    N, hex_num = input().split()
    N = int(N)

    binary_num = ''
    for n in hex_num:
        binary_num += hex_bin[n]
    
    print(f"#{test_case} {binary_num}")
