# 크로아티아 알파벳

alphabet = input()
N = len(alphabet)
ans = N
for i in range(N-1):
    if alphabet[i] == 'c' and alphabet[i+1] == '=':
        ans -= 1
    if alphabet[i] == 'c' and alphabet[i+1] == '-':
        ans -= 1
    if alphabet[i] == 'd' and alphabet[i+1] == '-':
        ans -= 1
    if alphabet[i] == 'l' and alphabet[i+1] == 'j':
        ans -= 1
    if alphabet[i] == 'n' and alphabet[i+1] == 'j':
        ans -= 1
    if alphabet[i] == 's' and alphabet[i+1] == '=':
        ans -= 1
    if alphabet[i] == 'z' and alphabet[i+1] == '=':
        ans -= 1
for j in range(N-2):
    if alphabet[j] == 'd' and alphabet[j+1] == 'z' and alphabet[j+2] == '=':
        ans -= 1

print(ans)