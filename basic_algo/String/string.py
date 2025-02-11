T = int(input())

for test_case in range(1, T+1):
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)
    found = 0

    for i in range(M-N+1):
        for j in range(N):
            if str1[j] != str2[i+j]:
                break

        else:
            found += 1
    print(f"#{test_case} {found}")