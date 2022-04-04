#음료수 얼려먹기
n,m=map(int,input().split())
data=[list(map(int,input())) for i in range(n)]
cnt=0

def dfs(x,y):
  if x<0 or x>n-1 or y<0 or y>m-1:
    return

  if data[x][y]==0:
    data[x][y]=1
    dfs(x+1,y)
    dfs(x,y+1)
    dfs(x-1,y)
    dfs(x,y-1)

for i in range(n):
  for j in range(m):
    if data[i][j]==0:
      dfs(i,j)
      cnt+=1

#print(*data,sep='\n')
print(cnt)