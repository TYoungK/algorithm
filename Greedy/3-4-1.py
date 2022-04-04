import time

n,k=map(int,input().split())
cnt=0
start_time=time.time()
while n!=1:
  if(n%k==0):
    n/=k
  else:
    n-=1
  cnt+=1
print(cnt)
print(f"time:{time.time()-start_time:.8f}")