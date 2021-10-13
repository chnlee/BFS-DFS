def dfs(graph,v,visited):
  visited[v] = True
  global count
  count +=1
  for i in graph[v]:
    if not visited[i]:
      visited[i] = True
      dfs(graph,i,visited)
v = int(input())
m = int(input())
count = 0
graph = [[] for _ in range(v+1)]
for x in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [False] * (v+1)
dfs(graph,1,visited)
print(count-1)
