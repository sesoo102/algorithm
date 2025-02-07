N = int(input())

def print_back(num):
    if num == 0:
        print(0)

    else:
        print(num, end = ' ')
        print_back(num - 1)

print_back(N)