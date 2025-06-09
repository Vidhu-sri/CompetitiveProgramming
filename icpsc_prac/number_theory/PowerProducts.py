
'''
You are given n
 positive integers a1,…,an
, and an integer k≥2
. Count the number of pairs i,j
 such that 1≤i<j≤n
, and there exists an integer x
 such that ai⋅aj=x^k
.

CodeForces
https://codeforces.com/contest/1225/problem/D
TechnoCup 2020 Round-2 D
'''

from collections import Counter

def build_spf(N):

    spf = [0]*(N+1)

    for i in range(2,N+1):
        if not spf[i]:
            for j in range(i,N+1,i):
                if not spf[j]:
                    spf[j] = i
    return spf


def rnc(x,k,spf): #reduce and complement
    red = 1
    comp = 1

    while x>1:
        p = spf[x]
        count = 0

        while x%p == 0:
            x//=p
            count+=1

        count %= k
        if count == 0:
            continue
        else:
            red*= p**count
            comp *= p**(k-count)
    return (red,comp)
        



n,k = map(int,input().split())
A = list(map(int,input().split()))

spf = build_spf(max(A))

freq = Counter()
ans = 0

for a in A:
    red,comp = rnc(a,k,spf)
    ans+= freq[comp]
    freq[red]+=1

print(ans)



