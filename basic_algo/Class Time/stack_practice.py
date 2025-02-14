# 스택을 구현해 봅시다.
# 구현한 스택을 이용하여 3개의 데이터를 스택에 저장하고 다시 3번 꺼내서 출력해 봅시다.

# 간단한 스택
top = -1
stack = [0] * 10

top += 1    # push 1
stack[top] = 1

top += 1    # push 2
stack[top] = 2

top += 1     # push 3
stack[top] = 3

top -= 1    # pop
print(stack[top + 1])

top -= 1    # pop
print(stack[top + 1])

top -= 1    # pop
print(stack[top + 1])