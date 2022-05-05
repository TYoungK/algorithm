#전보
import heapq
import sys

input=sys.stdin.readline
INF=int(1e9)

n,m,c=map(int,input().split())
g=[[] for _ in range(n+1)]
dis=[INF]*(n+1)

for _ in range(m):
  x,y,z=map(int,input().split())
  g[x].append((y,z))

q=[]
heapq.heappush(q,(0,c))
dis[c]=0

while q:
  d,now = heapq.heappop(q)
  if(dis[now]<d):
    continue
  for i in g[now]:
    cost=d+i[1]
    if dis[i[0]]>cost:
      dis[i[0]]=cost
      heapq.heappush(q,(cost,i[0]))


cnt=0
max_val=0
for i in dis:
  if i<INF:
    max_val=max(i,max_val)
    cnt+=1

print(cnt-1, max_val)