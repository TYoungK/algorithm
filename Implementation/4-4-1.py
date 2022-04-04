#게임 개발
n,m=map(int,input().split())
a,b,d=map(int,input().split())
data=[(list(map(int,input().split()))) for i in range(n)]
cnt=0
move=[[-1,0],[0,1],[1,0],[0,-1]]

while 1:
  block=1
  for mv in move:
    if data[a+mv[0]][b+mv[1]]==0:
      block=0

  if block==1:
    if data[a-move[d][0]][b-move[d][1]]==1: 
      break
    a=a-move[d][0]
    b=b-move[d][1]
  else:
    d-=1
    if d<0: d=3

    if data[a+move[d][0]][b+move[d][1]]==0: 
      a=a+move[d][0]
      b=b+move[d][1]
      data[a][b]=2
      cnt+=1

print(*data,sep='\n')
print(cnt,a,b)