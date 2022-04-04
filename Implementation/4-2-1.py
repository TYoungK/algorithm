#시각
#3을 포함하는 모든 시간의 갯수
#00:00:00 ~ n:59:59
import time
n=int(input())
cnt=0
start_time=time.time()
for h in range(n+1):
  for m in range(60):
    for s in range(60):
      if '3' in str(h)+str(m)+str(s):cnt+=1

print(cnt)
print(f"time:{time.time()-start_time:.8f}")
