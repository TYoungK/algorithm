#상하좌우
#최종 목적지 좌표 찾기

n=int(input())
plans=input().split()
x,y=1,1
dir={'U':[-1,0],'D':[1,0],'L':[0,-1],'R':[0,1]}


for plan in plans:
  c=[i+j for i,j in zip([x,y],dir.get(plan))]
  if c[0]>=1 and c[1]>=1 and c[0]<=n and c[1]<=n:
    x=c[0]
    y=c[1]

print(x,y)

  