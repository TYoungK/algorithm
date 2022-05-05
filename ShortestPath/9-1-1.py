#미래도시

n,m=map(int,input().split())

INF=int(1e9)
g=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
  for j in range(1,n+1):
    if i==j:
      g[i][j]=0

for _ in range(m):
  a,b=map(int,input().split())
  g[b][a]=1
  g[a][b]=1

x,k=map(int,input().split())



for i in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      g[a][b]=min(g[a][b],g[a][i]+g[i][b])

print(-1 if INF<=g[1][k]+g[k][x] else g[1][k]+g[k][x])
