T = int(input())


for tc in range(1, T+1):
    N = int(input())
    a = 1
    number = set()

    while len(number) < 10:
        aN = str(a*N)
        for i in range(len(aN)):
            number.add(aN[i])
        if len(number) < 10:
            a += 1
        
    print(f"#{tc} {aN}")