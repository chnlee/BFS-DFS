stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop() # FILO 구조에 따라 7이 제거됨을 알 수 있다.
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1])