#두 배열의 원소 교체
import time
import random
#n,k=map(int,input().split())
#a,b=[list(map(int,input().split()))for i in range(2)]
n=random.randrange(1,100000)
k=random.randrange(1,n)
a=[random.randrange(1,100000)]*n
b=[random.randrange(1,100000)]*n
print(n,k)
start_time=time.time()
for i in range(k):
  if min(a)<max(b):
    a.append(max(b))
    a.remove(min(a))
    b.append(min(a))
    b.remove(max(b))
  else:
    break
    
print(sum(a))
print(f"time:{time.time()-start_time:.8f}")

start_time=time.time()
a.sort()
b.sort(reverse=1)
for i in range(k):
  if a[i]<b[i]:
    a[i],b[i] = b[i],a[i]
  else:
    break

print(sum(a))
print(f"time:{time.time()-start_time:.8f}")