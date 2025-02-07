

# 가위 = 1, 바위 = 2, 보 = 3
# 1, 2 => 2 b   2, 1 => 2 a
# 2, 3 => 3 b   3, 2 => 3 a
# 3, 1 => 1 b   1, 3 => 1 a

a, b = map(int, input().split())

if a > b:
    if b==1 and a==3:
        print('B')
    
    else:
        print('A')

else:
    if a == 1 and b==3:
        print("A")
    
    else:
        print('B')
