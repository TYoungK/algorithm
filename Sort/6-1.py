#위에서 아래로
#n=[];exec("n.append(input());"*int(input()))
#print(*sorted(n),reverse=1)

print(*sorted([input() for i in range(int(input()))],reverse=1))
