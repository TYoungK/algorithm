#미로 탈출
from collections import deque
n,m=map(int,input().split())
maze=[list(map(int,input()))for i in range(n)]
dx,dy=[-1,1,0,0],[0,0,-1,1]
queue=deque()
queue.append([0,0])
distance=0
while queue:
  x,y=queue.popleft()
  if x==n-1 and y==m-1:
    distance=maze[x][y]
    break
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if nx>=n or nx<0 or ny>=m or ny<0:
      continue
    if maze[nx][ny]==1:
      queue.append([nx,ny])
      maze[nx][ny]=maze[x][y]+1

print(*maze,sep='\n')
print(distance)