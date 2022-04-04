import time
import cProfile

def logic():
  n,m,k=map(int,input().split())
  data=list(map(int,input().split()))
  start_time=time.time()
  i=max(data)
  data.remove(i)
  j=max(data)
  cnt=m//(k+1)*k+m%(k+1)
  print(i*cnt+j*(m-cnt))
  print(f"time:{time.time()-start_time:.8f}")

cProfile.run( 'logic()' )