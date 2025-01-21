
#if sums of A,B not equal -> NO
#if number of elements equal and arrays not identical -> NO
'''
you want to make b from A

f(b)  # can b be made from A elements

if b in A:
A.pop(A.index(b))
return True

if b even:
if count(b//2) >=2 in A:
pop both (b//2) and return True

else:
k = (b-1)//2
b = f(k) and f(k+1)

'''

from collections import Counter

N = int(input())

def f(counter,b):

    if b in counter and counter[b] >0:
        counter[b]-=1
        return True

    if b<=1:
        return False
    
    if not b%2:
        return f(counter,b//2) and f(counter,b//2)
    return f(counter,b//2) and f(counter,b//2+1)
        


for _ in range(N):
    n,m = map(int,input().split())
    A = sorted(list(map(int,input().split())))
    B = sorted(list(map(int,input().split())))

    
    if sum(A) != sum(B):
        print('NO')
        continue

    if len(A) == len(B):
        print('YES') if A==B else print('NO')
        continue
    counter = Counter(A)

    flag = True
    for b in B:
        if not f(counter,b):
            print('NO')
            flag = False
            break
    if flag:
        print('YES')
    
    
    

    
               