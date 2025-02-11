# Base 64 Decoding 코드
# Base4 인코딩된 문자열을 원래 문자열로 복원하는 Base64 디코딩을 수행한다.
T = int(input())

# Base64 인코딩 테이블 생성
decode = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
      'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
      '0','1','2','3','4','5','6','7','8','9','+','/' ]
'''
- Base64는 64개의 문자를 사용하여 데이터를 표현.
- decode 리스트는 Base64에서 사용되는 64개의 문자를 저장한 것이다.
- Base64 문자 -> 숫자로 변환할 때 이 리스트의 index()를 활용할 수 있다.
'''

for test_case in range(1, T + 1):
    # Base64로 인코딩된 문자열을 입력받아 리스트로 변환한다.
    word = list(input())

    # Base64 문자를 6비트 이진수로 변환
    value = ''
    for i in range(len(word)):
        num = decode.index(word[i])
        bin_num = str(bin(num)[2:])
        '''
        - Base64 문자를 6비트 이진수로 변환하는 과정.
        - decode.index(word[i])
            - decode 리스트에서 현재 문자의 인덱스(=Base64 값)를 찾는다.
            - ex) 'T' -> decode.index('T') = 19
        - bin(num)[2:]
            - 숫자를 이진수 문자열로 변환하고, 0b 접두사를 제거한다.
            - ex) bin(19) = '0b10011' -> '10011'
        '''

        # 6비트 맞추기(앞에 0을 채움)
        while len(bin_num) < 6:
            bin_num = '0' + bin_num
            '''
            - Base64에서 각 숫자는 6비트로 표현된다.
            - 만약 bin(num)을 6비트보다 짧게 변환하면 앞에 0을 추가하여 맞춰준다.
            - ex) bin(19) = '10011' (5비트) -> '010011' (6비트로 맞춤)
            '''

        # 변환된 이진수들을 연결(변환된 6비트 인지수를 하나의 문자열로 계속 연결한다.)
        value += bin_num

    # 8비트 단위로 변환(ASCII 문자 복원)
    result = ''
    for i in range(len(word)*6 // 8):
        data = int(value[i*8 : i*8+8], 2)
        result += chr(data)
    '''
    - 6비트 단위였던 문자열을 8비트 단위로 변환하여 ASCII 문자로 변환하는 과정이다.
    - len(word) * 6 // 8
        - Base64로 인코딩된 데이터는 6비트 단위로 되어 있으며, 원래 데이터는 8비트 단위이다.
        - 따라서 (전체 비트 수) / 8 을 하면 복원할 원래 문자 개수가 된다.
        - ex) 'TWFu' (24비트) -> 24/8 = 3 -> 'Man'
    - value[i * 8 : i * 8 + 8]
        - 8비트 단위로 슬라이싱하여 숫자로 변환한다.
        - ex) 010011 010110 000101 101110
            -> 8비트씩 나누면:
                01001101 (M) 01100001 (a) 01101110 (n)
    - int(value[i * 8 : i * 8 + 8], 2)
        - 이진수 -> 10진수 변환 (int(이진수, 2))
        - ASCII 문자로 변환 (chr(10진수))
    '''

    print(f'#{test_case} {result}')