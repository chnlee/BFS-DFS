# 단지 번호 붙이기 - bfs로 풀어보기
n = int(input())

graph = []
for i in range(n):
  graph.append(list(map(int,input())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

from collections import deque
def bfs(x,y):
  global count
  queue = deque()
  queue.append((x,y))
  graph[x][y] =0
  count = 1
  while queue:
    x,y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx <= -1 or nx >= n or ny <= -1 or ny >=n:
        continue
      if graph[nx][ny] == 0:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = 0
        queue.append((nx,ny))
        count += 1
  return count

_list = []
for i in range(n):
  for j in range(n):
     if graph[i][j] == 1:
         _list.append(bfs(i,j))

print(len(_list))
_list.sort()
for i in _list:
  print(i)