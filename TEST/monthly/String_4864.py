# 문자열 비교
def string_compare(str1, str2):
    n_1 = len(str1)
    n_2 = len(str2)
    found = 0

    for i in range(n_2 - n_1 + 1):
        for j in range(n_1):
            if str1[j] != str2[i + j]:  # 불일치 시 내부 루프 종료
                break
        else:
            found += 1  # 전체 루프를 돌았으면 부분 문자열 발견
    
    return found


# 입력 및 테스트 케이스 실행
T = int(input())
for test_case in range(1, T+1):
    str1 = input()
    str2 = input()

    ans = string_compare(str1, str2)

    print(f"#{test_case} {ans}")
