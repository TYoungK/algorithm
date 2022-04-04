#왕실의 나이트
data=input()
c,r=int(ord(data[0])-96),int(data[1])
cnt=0

for i in [-1,1]:
  for j in [-1,1]:
    for d in [[2,1],[1,2]]:
      next_c,next_r=c+d[0]*i,r+d[1]*j
      if next_c>0 and next_c<9 and next_r>0 and next_r<9:
          cnt+=1

print(cnt)