#도시 분할 계획
import sys

input=sys.stdin.readline

def find_parent(parent,x):
  if parent[x]!=x:
    parent[x]=find_parent(parent,parent[x])
  return parent[x]

def union(parent,x,y):
  a=find_parent(parent,x)
  b=find_parent(parent,y)
  if a<b:
    parent[b]=a
  else:
    parent[a]=b

n,m=map(int,input().split())
costs=[]
parent=[i for i in range(n+1)]
result=0
last=0
for _ in range(m):
  a,b,cost=map(int,input().split())
  costs.append((cost,a,b))

costs.sort()
print(costs)
for cost in costs:
  c,a,b=cost
  if find_parent(parent,a)!=find_parent(parent,b):
    union(parent,a,b)
    result+=c
    last=c


print(result,last)
print(result-last)
