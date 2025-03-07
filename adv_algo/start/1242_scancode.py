
hex_to_bin = {
    "0":"0000", "1":"0001", "2":"0010", "3":"0011",
    "4":"0100", "5":"0101", "6":"0110", "7":"0111",
    "8":"1000", "9":"1001", "A":"1010", "B":"1011",
    "C":"1100", "D":"1101", "E":"1110", "F":"1111"
}

decode = {
    '0001101' : '0',
    '0011001' : '1',
    '0010011' : '2',
    '0111101' : '3',
    '0100011' : '4',
    '0110001' : '5',
    '0101111' : '6',
    '0111011' : '7',
    '0110111' : '8',
    '0001011' : '9'
}

def hex_to_binary(hex_str):
    return ''.join(hex_to_bin[ch] for ch in hex_str)

T = int(input())
for test_case in range(1, T+1):
    # N 세로, M 가로
    N, M = map(int, input().split())
    arr = [input().strip() for _ in range(N)]
    
    # 2진수 추출 코드 저장
    binary_code = []
    
    # 16진수 >> 2진수
    binary_strings = []
    for row in arr:
        binary_strings.append(hex_to_binary(row))
    
    # print(binary_strings)


    # 2진수에서 암호 코드 찾기
    '''
    코드의 마지막 숫자를 이용해 암호코드의 가로 길이 구하기. 
    뒤에서부터 돌았을때 순서대로 1, 0, 1, 0의 개수 구하기기
    '''
    for r in range(N):
        for c in range(M * 4 - 1, -1, -1):  # 16진수에서 변환했으므로 4배 확장된 길이 고려
            if binary_strings[r][c] == '1':
                sr, sc = r, c
                
                # 암호 코드의 가로 길이 계산
                a1 = a2 = a3 = a4 = 0
                
                # 연속 패턴 카운트
                while c >= 0 and binary_strings[r][c] == '1':
                    a4 += 1
                    c -= 1
                
                while c >= 0 and binary_strings[r][c] == '0':
                    a3 += 1
                    c -= 1
                
                while c >= 0 and binary_strings[r][c] == '1':
                    a2 += 1
                    c -= 1
                
                while c >= 0 and binary_strings[r][c] == '0':
                    a1 += 1
                    c -= 1
                
               
                # a1~4을 이용해 56의 n 배수인지 확인
                n = (a1+a2+a3+a4) // 7
            
                binary_code.append([n, binary_strings[r][c-(56*n-1):c+1]])
                
                c -= (56*n)
    print(binary_code)            
            
    # 암호해독
    valid_codes = []
    for code in binary_code:
        n = code[0]
        b_code = code[1]
        

        if n == 0:
            continue

        digits = []

        for i in range(0, 56 * n, 7 * n):
            segment = b_code[i:i + (7 * n)]
            normalized_segment = ''.join(segment[j] for j in range(0, len(segment), n))
            if normalized_segment in decode:
                digits.append(int(decode[normalized_segment]))
        
        if len(digits) == 8:
            odd_sum = sum(digits[i] for i in range(0, 7, 2))
            even_sum = sum(digits[i] for i in range(1, 7, 2))
            check_digit = digits[7]
            
            if (odd_sum * 3 + even_sum + check_digit) % 10 == 0:
                valid_codes.append(sum(digits))
    
    print(f"#{test_case} {sum(valid_codes)}")         













    # # 0으로만 이루어진 행은 무시
        # 1번
        # non_zero = False
        # for ch in row:
        #     if ch != '0':
        #         non_zero = True
        #         break
        # if non_zero:
        #     binary_strings.add(hex_to_binary(row))
    # 2번
    # for row in arr:
    #     if any(ch != '0' for ch in row):  
    #         binary_strings.add(hex_to_binary(row))



    
    # print(f"#{test_case} {ans}") 
