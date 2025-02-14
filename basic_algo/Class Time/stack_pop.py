def pop():
    global top
    if top == -1:
        print('underflow')
        return 0
    else:
        top -= 1
        return stack[top + 1]

print(pop())

size = 10
stack = [0]*size
top = -1

# 간단 버전
if top > -1:
    top -= 1
    print(stack[top +1])