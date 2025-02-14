def push(item, size):
    global top
    top += 1
    if top == size: # 디버깅
        print('overflow!')
    else:
        stack[top] = item

size = 10
stack = [0]*size
top = -1

push(10, size)

# 간단버전
top += 1
stack[top]=20