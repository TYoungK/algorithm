#부품찾기
from sys import stdin

# def BinSearch(order,start,end):
#   if start>end:
#     return None
  
#   mid=(start+end)//2
  
#   if order==inven[mid]:
#     return True
#   elif order<inven[mid]:
#     return BinSearch(order,start,mid-1)
#   else:
#     return BinSearch(order,mid+1,end)

n=int(input())
inven=stdin.readline().rstrip().split()
m=input()
orders=stdin.readline().rstrip().split()

# for order in orders:
#   if BinSearch(order,0,0):
#     print('yes',end=' ')
#   else:
#     print('no',end=' ')

# for order in orders:
#   if order in inven:
#     print('yes',end=' ')
#   else:
#     print('no',end=' ')