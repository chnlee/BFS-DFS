# bfs 메서드 정의
from collections import deque
def bfs(graph, start, visited):
  # 큐 구현을 위해 덱 라이브러리 사용
  queue = deque([start])
  visited[start] = True
  # 큐가 빌 때까지 반복
  while queue:
    #큐에서 하나의 원소를 뽑아 출력
    v = queue.popleft()
    print(v,end=' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

# 각 노드가 방문한 정보를 리스트 자료형으로 표현
visited = [False] * 9

# 정의된 DFS 함수 호출
bfs(graph,1,visited)