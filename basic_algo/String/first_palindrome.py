T = int(input())

for test_case in range(1, T+1):
    words = input()
    found = 0


    for i in range(len(words)//2):
        if words[i] != words[len(words)-i-1]:
            break
    
    else:
        found = 1
    
    print(f'#{test_case} {found}')
