import sys
sys.setrecursionlimit(10 ** 4)
T = int(input())
_list = []
def dfs(x,y):
  if x <= -1 or y <= -1 or x >= N or y >= M:
    return False
  if graph[x][y] == 1:
    graph[x][y] = 0
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    return True
  return False

for i in range(T):
  M, N, K = map(int,input().split())
  graph = [[0] * M for _ in range(N)]
  for j in range(K):
    a,b = (map(int,input().split()))
    graph[b][a] = 1
  result = 0
  for p in range(N):
    for q in range(M):
      if dfs(p,q) == True:
        result += 1
        
  _list.append(result)

for i in range(len(_list)):
  print(_list[i])
