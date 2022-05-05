#커리큘럼
import sys
from collections import deque
import copy

input=sys.stdin.readline
n=int(input())
g=[[]for i in range(n+1)]
indgree=[0]*(n+1)
time=[0]*(n+1)
for i in range(1,n+1):
  data=list(map(int,input().split()))
  time[i]=data[0]
  for j in data[1:-1]:
    indgree[i]+=1  
    g[j].append(i)
  
q=deque()
result=copy.deepcopy(time)

for i in range(1,n+1):
    if indgree[i]==0:
      q.append((i))
      
while q:
  now=q.popleft()
  
  for i in g[now]:
    result[i]=max(result[i],result[now]+time[i])
    indgree[i]-=1
    if indgree[i]==0:
      q.append(i)
  

for i in result:
  if i!=0:
    print(i) 