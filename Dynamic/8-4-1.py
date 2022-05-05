#효율적인 화폐 구성
#N개의 화폐 종류로 M원 만들기

n,m=map(int,input().split())
x=[int(input()) for i in range(n)]
d=[10001]*(m+1)
d[0]=0
for i in range(m+1):
  for j in range(n):
    d[i]=min(d[i-x[j]]+1,d[i])


print(d[m] if d[m]!=10001 else -1)