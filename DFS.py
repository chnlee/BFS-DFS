#DFS/BFS
adjacency matrix
INF = 999999999

graph = [[0,7,5],[7,0,INF],[5,INF,0]]
print(graph)
# adjacency list
graph = [[] for _ in range(3)]

graph[0].append((1,7))
graph[0].append((2,5))

graph[1].append((0,7))

graph[2].append((0,5))

print(graph)

# dfs 메서드 정의

def dfs(graph, v, visited):
  # 현재 노드를 방문 처리
  visited[v] = True
  print(v, end =' ')
  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

# 각 노드가 방문한 정보를 리스트 자료형으로 표현
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph,1,visited)