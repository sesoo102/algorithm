T = int(input())


for tc in range(1, T + 1):
    str1 = list(input())
    str2 = list(input())
    result = []

    for char in str1:
        cnt = 0
        for s in str2:
            if char == s:
                cnt += 1
        result.append(cnt)
    
    max_cnt = 0
    for num in result:
        if max_cnt < num:
            max_cnt = num
    
    print(f"#{tc} {max_cnt}")
