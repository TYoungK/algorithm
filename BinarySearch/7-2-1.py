#떡 자르기
from sys import stdin

def Cut(start,end):
  if start>end:
    return None
  mid=(start+end)//2
  total=0
  
  for i in list:
    if i>mid:
      total+=i-mid
      
  if total<m:
    return Cut(start,mid-1)
  else:
    global result
    if result<mid:
      result=mid
    return Cut(mid+1,end)

n,m=map(int,input().split())
list=list(map(int,stdin.readline().rstrip().split()))
result=0
Cut(0,max(list)-1)
print(result)

