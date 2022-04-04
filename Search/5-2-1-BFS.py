#BFS 큐 사용
from collections import deque

def bfs(graph,v,visited):
  queue=deque([v])
  visited[v]=True
  while queue:
    v=queue.popleft()
    print(v,end=' ')
    for g in graph[v]:
      if not visited[g]:
        queue.append(g)
        visited[g]=True
  
graph=[
  [],
  [2,3,8],
  [1,7],
  [1,4,5],
  [3,5],
  [3,4],
  [7],
  [2,6,8],
  [1,7]
]

visited = [False]*9

bfs(graph,1,visited)