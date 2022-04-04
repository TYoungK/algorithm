#DFS 재귀 함수

def dfs(graph,v,visitied):
  visited[v]=True
  print(v,end=' ')
  for g in graph[v]:
    if not visited[g]:
      dfs(graph,g,visited)
    
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

dfs(graph,1,visited)