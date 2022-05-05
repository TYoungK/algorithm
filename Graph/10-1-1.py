#팀 결성
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
    parent[b]=b
  else:
    parent[a]=a
  return 

n,m=map(int,input().split())
parent=[i for i in range(n+1)]

for _ in range(m):
  method,a,b=map(int,input().split())
  
  if find_parent(parent,a) == find_parent(parent,b):
    if method:
      print("YES")
  else:
    if method:
      print("NO")  
    else:
      union(parent,a,b)


