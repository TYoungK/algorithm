#성적이 낮은 순서로 학생 출력
print(*list(map(list,zip(*sorted([input().split()for i in range(int(input()))],key=lambda s:int(s[1])))))[0])