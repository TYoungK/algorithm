n,m=map(int,input().split())
rs=0
for i in range(n):
  minval=min(map(int,input().split()))
  if rs<minval:
    rs=minval
print(rs)