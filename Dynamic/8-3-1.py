#타일링
n=int(input())
d=[1]*10
d[2]=3

for i in range(3,n+1):
  d[i]=d[i-1]+d[i-2]*2

print(d[n]%796796)