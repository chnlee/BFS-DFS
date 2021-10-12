# DFS와 BFS

#DFS 만들기
def dfs(graph,v,visited):
  visited[v] = True
  print(v,end=' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited)
#BFS 만들기
from collections import deque

def bfs(graph,start,visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    print(v,end=' ')
    for i in graph[v]:
      if not visited[i]:
        visited[i] = True
        queue.append(i)
n, m, v = map(int,input().split())
number = []
for i in range(m):
  number.append(list(map(int,input().split())))
# 그래프를 만드는 과정
graph = [[] for _ in range(n+1)]
def make_graph(x):
  global graph
  val1 = number[x][0]
  val2 = number[x][1]
  if val1 not in graph[val2]:
    graph[val2].append(val1)
  if val2 not in graph[val1]:
    graph[val1].append(val2)
for x in range(m):  
  make_graph(x)
for i in range(n+1):
  graph[i].sort()  
# 각 노드가 방문한 정보를 False로 표현한다.
visited = [False] * (n+1)
dfs(graph,v,visited)
visited = [False] * (n+1)
print()
bfs(graph,v,visited)
