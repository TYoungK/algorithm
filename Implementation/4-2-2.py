#시각
#복잡도 줄이기
import time
n=int(input())
cnt=0
start_time=time.time()

for h in range(1):
  for m in range(60):
    for s in range(60):
      if '3' in str(h)+str(m)+str(s):cnt+=1

#n이 3,13,23포함 여부
x=0
if n>=3:
  x+=1
  if n>=13:
    x+=1
    if n>=23:
      x+=1
print(cnt,x,cnt*(n-x+1)+x*3600)
print(f"time:{time.time()-start_time:.8f}")


#23입력 기준 0.13583493에서 0.00318241로 단축