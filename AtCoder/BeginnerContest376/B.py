N,Q = tuple(map(int,input().split()))

l,r = 1,2
res = 0
ring = [*range(1,N)]
for _ in range(Q):
    H,T = list(input().split())
    T = int(T)
    other =  r if H == 'L' else l
    hand = r if H == 'R' else l

    if min(other,hand) < T < max(other,hand):
        res+= N-max(other,hand) + min(other, hand)
        
    else:
        res+= T-min(other,hand)
    if H == 'R':
            r = T
    else:
        l = T
   
print(res)
        

