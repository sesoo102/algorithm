N = int(input())
arr = list(map(int, input().split()))
 
middle = N // 2
 
print(sorted(arr)[middle])