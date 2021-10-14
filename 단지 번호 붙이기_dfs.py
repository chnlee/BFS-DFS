# 단지 번호 붙이기 - bfs로 풀어보기
n = int(input())

graph = []
for i in range(n):
  graph.append(list(map(int,input())))
def dfs(x,y):
  global count
  if x <= -1 or x >= n or y <= -1 or y >=n:
    return False
  if graph[x][y] == 1:
    count += 1
    graph[x][y] = 0
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    return True
  return False
count = 0
_list = []
for i in range(n):
  for j in range(n):
    if dfs(i,j) == True:
      _list.append(count)
      count = 0
print(len(_list))
_list.sort()
for i in _list:
  print(i)

