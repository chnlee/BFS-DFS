# 컬렉션 모듈에서 제공하는 deque 자료 구조 활용

from collections import deque

#큐 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 원소 순서 대로 출력 -> 3714
queue.reverse() 
print(queue) # 4173