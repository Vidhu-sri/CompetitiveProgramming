# EDITORIAL SOLUTION WITH PREFIX SUM


import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
sint = lambda: int(input())
mint = lambda: map(int, input().split())
aint = lambda: list(map(int, input().split()))
###############################################
t = sint()
for _ in range(t):
    n,d,k=mint()
    ct=[0]*(n+2)
    for _ in range(k):
        L,R=mint()
        ct[max(1,L-d+1)]+=1
        ct[R+1]-=1
    cur=0
    mn=10**6;mni=0
    mx=-1;mxi=0
    for i in range(1,n-d+2):
        cur+=ct[i]
        if cur<mn:mn=cur;mni=i
        if cur>mx:mx=cur;mxi=i
    print(mxi,mni)