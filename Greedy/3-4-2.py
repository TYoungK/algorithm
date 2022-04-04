import time

n,k=map(int,input().split())
cnt=0
start_time=time.time()
while n>=k:
  cnt+=n%k+1
  n//=k

print(cnt+n-1)
print(f"time:{time.time()-start_time:.8f}")